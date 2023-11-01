# Copyright (c) 2023, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import glob
import hashlib
import os
import shutil
import sys

# These are undocumented internals until SIP implements a proper documentation
# system.
from sipbuild.generator import parse, resolve
from sipbuild.generator.outputs.xml import output_xml


class FixedIndenter:
    """ The implementation of a indenter that indents by a fixed amount. """

    def indent(self, f):
        """ Write the indent. """

        f.write('    ')


class ListItemIndenter:
    """ The implementation of a indenter that indents list items. """

    def __init__(self, item_prefix):
        """ Initialise the object. """

        self._item_prefix = item_prefix

    def indent(self, f):
        """ Write the indent. """

        f.write(self._item_prefix + ' ')
        self._item_prefix = ' ' * len(self._item_prefix)


class Formatter:
    """ A class for formatting output written to a file. """

    def __init__(self, fname):
        """ Initialise the object. """

        self.fname = fname
        self.fd = None
        self.buffer = ''

        self._indenters = []
        self.escape_dquotes = False

    def deindent(self):
        """ De-indent subsequent text. """

        self.flush()

        try:
            old_indenter = self._indenters.pop()
        except IndexError:
            old_indenter = None

        return old_indenter

    def flush(self):
        """ Make sure any pending in-line text is written with a newline. """

        pending = self.buffer.rstrip()
        self.buffer = ''

        if pending:
            self._write_indented_line(pending)

    def indent(self, indenter=FixedIndenter()):
        """ Indent subsequent text. """

        self.flush()

        if indenter is not None:
            self._indenters.append(indenter)

    def write_inline(self, text, leading_blank=True):
        """ Write some text in-line. """

        # Precede the start of a 'paragraph' with a blank line.
        if leading_blank and not self.buffer:
            self.fd.write('\n')

        if self.escape_dquotes:
            text = text.replace('"', '""')

        self.buffer += text

    def write_line(self, text='', leading_blank=True):
        """ Write some text as a single line. """

        self.flush()

        if text:
            if leading_blank:
                self.fd.write('\n')

            self._write_indented_line(text)
        else:
            self.fd.write('\n')

    def _write_indented_line(self, line):
        """ Write an indented line. """

        for indenter in self._indenters:
            indenter.indent(self.fd)

        self.fd.write(line)
        self.fd.write('\n')


class ObjectName:
    """ Encapsulate the name of a Python object that may have a different C/C++
    name.
    """

    def __init__(self, el, object_type):
        """ Initialise the object. """

        # For modules, el is actually the module name.
        if object_type == 'm':
            self.py_name = el
            real_name = None
        else:
            # This is the Python name relative to the containing module.
            self.py_name = el.attrib['name']

            # Only remember the real name if it is different to (ie. can't be
            # derived from) the Python one.
            real_name = el.attrib.get('realname')
            if real_name:
                if self.py_name.split('.') == real_name.split('::'):
                    real_name = None

        self.real_name = real_name

        # This is the name of any description file excluding any unique
        # identifer and the file extension.
        self.description_name = self.py_name.replace('.', '-') + '-' + object_type

        # This is the name of any API file excluding the file extension.
        self.api_name = self.py_name.replace('.', '-').lower()

        if object_type == 'm':
            self.api_name += '-module'

        self.object_type = object_type


class Method:
    """ Encapsulate a method and all its overloads. """

    _all_methods = {}

    def __init__(self, name):
        """ Initialise the object. """

        self.name = name
        self.overloads = []

    @classmethod
    def find(cls, name):
        """ Return the method for a name creating it if necessary. """

        meth = cls._all_methods.get(name.py_name)
        if meth is None:
            meth = Method(name)
            cls._all_methods[name.py_name] = meth

        return meth


class TypedValue:
    """ Encapsulate a typed value, eg. a method argument or result. """

    def __init__(self, py_type):
        """ Initialise the object. """

        self.py_type = py_type


class Overload:
    """ Encapsulate a method overload. """

    def __init__(self, static=False, cppsig=None):
        """ Initialise the object. """

        self.static = static
        self.realsig = cppsig
        self.args = []
        self.returns = []


def generate_rst(module, package, descriptions, api, sip_file, include_dirs,
        verbose):
    """ Generate the reST for a single module. """

    # Create the module-specific api directory.
    api = os.path.join(api, module.lower())
    os.makedirs(api, exist_ok=True)

    os.makedirs(os.path.join(descriptions, module), exist_ok=True)

    if sip_file is None:
        module_el = None
    else:
        encoding = 'UTF-8'

        spec, modules, _ = parse(sip_file, hex_version=0x600000,
                encoding=encoding, abi_version='13.0', tags=[],
                disabled_features=['PyQt_OpenGL_ES2'],
                protected_is_public=False, include_dirs=include_dirs,
                sip_module='PyQt6.sip', is_strict=False)

        resolve(spec, modules)
        module_el = output_xml(spec, module)

    # Generate the reST for the module.
    fq_module = '{}.{}'.format(package, module) if package else module

    generate_module_rst(module_el, module, fq_module, descriptions, api,
            verbose)

    if module_el is not None:
        # Generate the reST for each class.
        for el in module_el:
            if el.tag == 'Class' and 'extends' not in el.attrib:
                generate_class_rst(el, module, fq_module, descriptions, api,
                        verbose)


def generate_module_rst(module_el, module, fq_module, descriptions, api, verbose):
    """ Generate the reST for a single module. """

    if verbose:
        progress("Generating skeleton for {}...".format(module))

    name = ObjectName(module, 'm')
    assert name.py_name == module

    api_fmt = Formatter(os.path.join(api, name.api_name + '.rst'))

    with open(api_fmt.fname, 'w') as api_fmt.fd:
        api_fmt.write_line(':orphan:', leading_blank=False)

        api_fmt.write_line('.. sip:module:: {}'.format(fq_module))

        api_fmt.indent()

        # Include the description file.
        desc_path, desc_rel = make_description_name(descriptions, module, name)

        api_fmt.write_line(':description: {}'.format(desc_rel),
                leading_blank=False)

        api_fmt.deindent()

        # Create the description file if it doesn't already exist.
        if not os.path.lexists(desc_path):
            desc_fmt = Formatter(desc_path)

            with open(desc_fmt.fname, 'w') as desc_fmt.fd:
                desc_fmt.write_line('.. sip:module-description::',
                        leading_blank=False)

                desc_fmt.indent()
                desc_fmt.write_line(':status: todo', leading_blank=False)
                desc_fmt.write_line(':brief:  TODO', leading_blank=False)
                desc_fmt.deindent()

                desc_fmt.write_line('TODO')

        if module_el is not None:
            generate_scope_rst(module_el, module, fq_module, descriptions,
                    api_fmt, verbose)


def generate_class_rst(class_el, module, fq_module, descriptions, api, verbose):
    """ Generate the reST for a single class. """

    name = ObjectName(class_el, 'c')

    if verbose:
        progress("Generating skeleton for {}...".format(name.py_name))

    # See if it is a QFlags class.
    flags_enums = class_el.attrib.get('flagsenums')

    api_fmt = Formatter(os.path.join(api, name.api_name + '.rst'))

    with open(api_fmt.fname, 'w') as api_fmt.fd:
        api_fmt.write_line(':orphan:', leading_blank=False)

        api_fmt.write_line(
                '.. sip:class:: {}.{}'.format(fq_module, name.py_name))

        api_fmt.indent()

        # Handle any super-classes.
        inherits = class_el.attrib.get('inherits')
        if inherits:
            api_fmt.write_line(':inherits: {}'.format(inherits),
                    leading_blank=False)

        # Include the description file.
        desc_path, desc_rel = make_description_name(descriptions, module, name)

        api_fmt.write_line(':description: {}'.format(desc_rel),
                leading_blank=False)

        api_fmt.deindent()

        # Create the description file if it doesn't already exist.
        if not os.path.lexists(desc_path):
            desc_fmt = Formatter(desc_path)

            with open(desc_fmt.fname, 'w') as desc_fmt.fd:
                desc_fmt.write_line('.. sip:class-description::',
                        leading_blank=False)

                if flags_enums is None:
                    desc_fmt.indent()
                    desc_fmt.write_line(':status: todo', leading_blank=False)
                    desc_fmt.write_line(':brief:  TODO', leading_blank=False)
                    generate_real_name(desc_fmt, name)
                    desc_fmt.deindent()

                    desc_fmt.write_line('TODO')
                else:
                    # Provide a canned description for QFlags based classes.
                    desc_fmt.indent()
                    desc_fmt.write_line(':status: done', leading_blank=False)
                    generate_real_name(desc_fmt, name)
                    desc_fmt.deindent()

                    flags_enums = flags_enums.split(' ')

                    if len(flags_enums) == 1:
                        enums = ":sip:ref:`~{}.{}` enum".format(fq_module,
                                flags_enums[0])
                    else:
                        enums = ', '.join(
                                [":sip:ref:`~{}.{}`".format(fq_module, e)
                                        for e in flags_enums[:-1]])

                        enums += " and :sip:ref:`~{}.{}` enums".format(
                                fq_module, flags_enums[-1])

                    text = "The :sip:ref:`~{}.{}` class is a set of flags whose values are the members of the {}. Instances of the class support the standard Python ``int`` methods.".format(fq_module, name.py_name, enums)
                    desc_fmt.write_line(text)

        if flags_enums is None:
            generate_scope_rst(class_el, module, fq_module, descriptions,
                    api_fmt, verbose)


def generate_scope_rst(scope_el, module, fq_module, descriptions, api_fmt, verbose):
    """ Generate the reST for Python objects contained in a single scope. """

    api_fmt.indent()

    # Handle the enums.
    generate_enums_rst(scope_el, module, fq_module, descriptions, api_fmt,
            verbose)

    # Handle the attributes.
    generate_attrs_rst(scope_el, module, fq_module, descriptions, api_fmt,
            verbose)

    # Handle the methods.
    generate_methods_rst(scope_el, module, fq_module, descriptions, api_fmt,
            verbose)

    # Handle the signals.
    generate_signals_rst(scope_el, module, fq_module, descriptions, api_fmt,
            verbose)

    api_fmt.deindent()


def generate_enums_rst(scope_el, module, fq_module, descriptions, api_fmt, verbose):
    """ Generate the reST for the enums in a scope. """

    # Get the sorted list of enums.
    py_enums = []

    for enum_el in scope_el:
        if enum_el.tag == 'Enum':
            # Get the sorted list of members.
            members = []

            for member_el in enum_el:
                if member_el.tag == 'EnumMember':
                    members.append(ObjectName(member_el, 'v'))

            members.sort(key=lambda m: m.py_name.lower())

            py_enums.append((ObjectName(enum_el, 'e'), members))

    py_enums.sort(key=lambda e: e[0].py_name.lower())

    # Generate the skeleton for the enums.
    for name, members in py_enums:
        api_fmt.write_line(
                '.. sip:enum:: {}.{}'.format(fq_module, name.py_name))

        # Include the description file.
        desc_path, desc_rel = make_description_name(descriptions, module, name)

        api_fmt.indent()
        api_fmt.write_line(':description: {}'.format(desc_rel),
                leading_blank=False)

        # Create the description file if it doesn't already exist.
        if not os.path.lexists(desc_path):
            desc_fmt = Formatter(desc_path)

            with open(desc_fmt.fname, 'w') as desc_fmt.fd:
                desc_fmt.write_line('.. sip:enum-description::',
                        leading_blank=False)

                desc_fmt.indent()

                desc_fmt.write_line(':status: todo', leading_blank=False)
                generate_real_name(desc_fmt, name)
                desc_fmt.deindent()

                desc_fmt.write_line('TODO')

        # Create description files for each member.
        for member in members:
            api_fmt.write_line(
                    '.. sip:enum-member:: {}.{}'.format(fq_module,
                            member.py_name))

            m_desc_path, m_desc_rel = make_description_name(descriptions,
                    module, member)

            api_fmt.indent()
            api_fmt.write_line(':description: {}'.format(m_desc_rel),
                    leading_blank=False)
            api_fmt.deindent()

            if not os.path.lexists(m_desc_path):
                m_desc_fmt = Formatter(m_desc_path)

                with open(m_desc_fmt.fname, 'w') as m_desc_fmt.fd:
                    m_desc_fmt.write_line('.. sip:enum-member-description::',
                            leading_blank=False)

                    m_desc_fmt.indent()

                    m_desc_fmt.write_line(':status: todo', leading_blank=False)
                    m_desc_fmt.write_line(':value: TODO', leading_blank=False)
                    generate_real_name(m_desc_fmt, member)
                    m_desc_fmt.deindent()

                    m_desc_fmt.write_line('TODO')

        api_fmt.deindent()


def generate_attrs_rst(scope_el, module, fq_module, descriptions, api_fmt, verbose):
    """ Generate the reST for the attributes in a scope. """

    # Get the sorted list of attributes.
    py_attrs = []

    for attr_el in scope_el:
        if attr_el.tag == 'Member':
            py_attrs.append(
                    (ObjectName(attr_el, 'a'),
                            TypedValue(attr_el.attrib['typename']),
                            attr_el.attrib.get('const'),
                            attr_el.attrib.get('static')))

    py_attrs.sort(key=lambda a: a[0].py_name.lower())

    # Generate the skeleton for the attributes.
    for name, type_name, const, static in py_attrs:
        api_fmt.write_line(
                '.. sip:attribute:: {}.{}'.format(fq_module, name.py_name))

        api_fmt.indent()

        api_fmt.write_line(':type: {}'.format(type_name.py_type),
                leading_blank=False)

        if const:
            api_fmt.write_line(':const:', leading_blank=False)

        if static:
            api_fmt.write_line(':static:', leading_blank=False)

        # Include the description file.
        desc_path, desc_rel = make_description_name(descriptions, module, name)

        api_fmt.write_line(':description: {}'.format(desc_rel),
                leading_blank=False)

        api_fmt.deindent()

        # Create the description file if it doesn't already exist.
        if not os.path.lexists(desc_path):
            desc_fmt = Formatter(desc_path)

            with open(desc_fmt.fname, 'w') as desc_fmt.fd:
                desc_fmt.write_line('.. sip:attribute-description::',
                        leading_blank=False)

                desc_fmt.indent()
                desc_fmt.write_line(':status: todo', leading_blank=False)
                generate_real_name(desc_fmt, name)
                desc_fmt.deindent()

                desc_fmt.write_line('TODO')


def generate_methods_rst(scope_el, module, fq_module, descriptions, api_fmt, verbose):
    """ Generate the reST for the methods in a scope. """

    # Get the lists of methods.  We have separate lists for __init__().
    init = None
    methods = []

    for meth_el in scope_el:
        if meth_el.tag != 'Function':
            continue

        # TODO: handle slot extenders.
        if 'extends' in meth_el.attrib:
            continue

        meth = Method.find(ObjectName(meth_el, 'f'))

        if meth.name.py_name.endswith('.__init__'):
            init = meth
        elif meth not in methods:
            methods.append(meth)

        static = (scope_el.tag == 'Class' and meth_el.attrib.get('static'))

        oload = Overload(static=static, cppsig=meth_el.attrib.get('cppsig'))
        meth.overloads.append(oload)

        for arg_el in meth_el:
            if arg_el.tag == 'Argument':
                oload.args.append(TypedValue(arg_el.attrib['typename']))
            elif arg_el.tag == 'Return':
                oload.returns.append(TypedValue(arg_el.attrib['typename']))

    # Sort the names.
    methods.sort(key=lambda m: m.name.py_name.replace('__', '').lower())

    # Any __init__ methods go at the start.
    if init is not None:
        methods.insert(0, init)

    # Generate the skeleton for the methods.
    for meth in methods:
        # Show the simpler overloads first.
        meth.overloads.sort(key=lambda o: len(o.args))

        pysigs = get_pysigs(descriptions, module, meth.name)

        for oload in meth.overloads:
            api_fmt.write_line(
                    '.. sip:method:: {}.{}'.format(fq_module,
                            meth.name.py_name))

            api_fmt.indent()

            # Generate a digest for the Python signature.
            pysig_md5 = hashlib.new('md5')

            if oload.args:
                api_fmt.write_line( ':args:', leading_blank=False)

                api_fmt.indent()

                for arg in oload.args:
                    api_fmt.write_line('{}'.format(arg.py_type),
                            leading_blank=False)
                    pysig_md5.update(arg.py_type.encode('utf8'))

                api_fmt.deindent()

            if oload.returns:
                api_fmt.write_line( ':returns:', leading_blank=False)

                api_fmt.indent()

                for ret in oload.returns:
                    api_fmt.write_line('{}'.format(ret.py_type),
                            leading_blank=False)
                    pysig_md5.update(ret.py_type.encode('utf8'))

                api_fmt.deindent()

            if oload.static:
                api_fmt.write_line(':static:', leading_blank=False)
                pysig_md5.update(b'static')

            handle_description(oload.realsig, pysigs, pysig_md5, meth.name,
                    module, fq_module, descriptions, api_fmt)


def generate_signals_rst(scope_el, module, fq_module, descriptions, api_fmt, verbose):
    """ Generate the reST for the signals in a scope. """

    signals = []

    for sig_el in scope_el:
        if sig_el.tag == 'Signal':
            sig = Method.find(ObjectName(sig_el, 's'))

            if sig not in signals:
                signals.append(sig)

            oload = Overload(cppsig=sig_el.attrib.get('cppsig'))
            sig.overloads.append(oload)

            for arg_el in sig_el:
                if arg_el.tag == 'Argument':
                    oload.args.append(TypedValue(arg_el.attrib['typename']))

    # Sort the names.
    signals.sort(key=lambda s: s.name.py_name.lower())

    # Generate the skeleton for the signals.
    for sig in signals:
        pysigs = get_pysigs(descriptions, module, sig.name)

        # Note that we don't sort the overloads as the order is significant.
        for oload in sig.overloads:
            api_fmt.write_line(
                    '.. sip:signal:: {}.{}'.format(fq_module,
                            sig.name.py_name))

            api_fmt.indent()

            # Generate a digest for the Python signature.
            pysig_md5 = hashlib.new('md5')

            if oload.args:
                api_fmt.write_line( ':args:', leading_blank=False)

                api_fmt.indent()

                for arg in oload.args:
                    api_fmt.write_line('{}'.format(arg.py_type),
                            leading_blank=False)
                    pysig_md5.update(arg.py_type.encode('utf8'))

                api_fmt.deindent()

            handle_description(oload.realsig, pysigs, pysig_md5, sig.name,
                    module, fq_module, descriptions, api_fmt)


def generate_real_name(desc_fmt, name):
    """ Generate the real name for the documentation extractor if it is
    different to the Python name.
    """

    if name.real_name:
        desc_fmt.write_line(':realname: {}'.format(name.real_name),
                leading_blank=False)


def handle_description(realsig, pysigs, pysig_md5, name, module, fq_module, descriptions, api_fmt):
    """ Handle the name of the description file and the creation (if necessary)
    of the file itself.
    """

    # See if there is already a description file for this Python signature.
    pysig = pysig_md5.hexdigest()

    for file_nr, digest in pysigs.items():
        if digest == pysig:
            no_desc_file = False
            break
    else:
        no_desc_file = True

        # Allocate an unused file number.
        file_nr = 0
        while file_nr in pysigs:
            file_nr += 1

        # This number is now allocated.
        pysigs[file_nr] = pysig

    # Add the name of the description file.
    desc_path, desc_rel = make_description_name(descriptions, module, name,
            unique=file_nr)

    api_fmt.write_line(':description: {}'.format(desc_rel),
            leading_blank=False)

    api_fmt.deindent()

    # Create the description file if it doesn't already exist.
    if no_desc_file:
        desc_fmt = Formatter(desc_path)

        with open(desc_fmt.fname, 'w') as desc_fmt.fd:
            desc_fmt.write_line(
                    '.. sip:{}-description::'.format(
                            'signal' if name.object_type == 's' else 'method'),
                    leading_blank=False)

            desc_fmt.indent()

            desc_fmt.write_line(':status: todo', leading_blank=False)

            # Tell the Sphinx extension what the Python signature is.
            desc_fmt.write_line(':pysig: {}'.format(pysig),
                    leading_blank=False)

            # Tell any extractor what the real signature is.
            generate_real_name(desc_fmt, name)

            if realsig:
                desc_fmt.write_line(':realsig: {}'.format(realsig),
                    leading_blank=False)

            desc_fmt.deindent()

            desc_fmt.write_line('TODO')


def clean_skeletons(module, api, verbose):
    """ Remove all API skeletons for a specific module. """

    module_api = os.path.join(api, module.lower())

    if verbose:
        progress("Removing {}".format(module_api))

    shutil.rmtree(module_api, ignore_errors=True)


def clean_descriptions(module, descriptions, verbose):
    """ Remove all unmodified description files for a specific module. """

    for desc in glob.glob(os.path.join(descriptions, module, '*.rst')):
        has_status = False
        status_todo = True

        with open(desc, 'rt') as f:
            for line in f:
                parts = line.split(maxsplit=3)
                if len(parts) == 2 and parts[0] == ':status:':
                    has_status = True

                    if parts[1] != 'todo':
                        status_todo = False
                        break

        if has_status and status_todo:
            # The file contains at least one :status: and all of them are
            # 'todo'.
            if verbose:
                progress("Removing {}".format(desc))

            os.remove(desc)


def make_description_name(descriptions, module, name, pattern=False, unique=0):
    """ Return a 2-tuple of the absolute pathname of a description file for a
    C/C++ object and it's name relative to the root descriptions directory.
    """

    if pattern:
        suffix = '*'
    elif unique > 0:
        suffix = '-' + str(unique)
    else:
        suffix = ''

    fname = '{}{}.rst'.format(name.description_name, suffix)

    rel_path = os.path.join(module, fname)
    path = os.path.join(descriptions, rel_path)

    return path, rel_path


def get_pysigs(descriptions, module, name):
    """ Return a dict of the Python signature digest keyed by the unique
    file number for each overload with a description.
    """

    desc_pattern, _ = make_description_name(descriptions, module, name,
            pattern=True)

    pysigs = {}

    for desc in glob.glob(desc_pattern):
        # Get the digest.
        pysig = None

        with open(desc) as fd:
            for line in fd:
                parts = line.strip().split()
                if len(parts) == 2 and parts[0] == ':pysig:':
                    pysig = parts[1]
                    break

        # Get the file number.
        file_nr = -1

        parts = desc[:-4].split('-')

        if parts[-1] == name.object_type:
            file_nr = 0
        else:
            try:
                file_nr = int(parts[-1])
            except ValueError:
                file_nr = -1

        # Save if both are valid.
        if pysig is not None and file_nr >= 0:
            pysigs[file_nr] = pysig

    return pysigs


def error(message):
    """ Write an error message to stderr and terminate with a non-zero exit
    code.
    """

    program_name = os.path.basename(sys.argv[0])
    sys.stderr.write("{}: {}\n".format(program_name, message))
    sys.exit(1)


def progress(message):
    """ Write a progress message to stdout. """

    print(message, flush=True)


if __name__ == '__main__':

    # Parse the command line.
    import argparse

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--api', metavar='DIR',
            default=os.path.join('docs', 'api'),
            help="the name of the directory where the module's API .rst files will be placed")

    arg_parser.add_argument('--clean', action='store_true', default=False,
            help="remove any unmodified (todo) stub description files")

    arg_parser.add_argument('--descriptions', metavar='DIR',
            default='descriptions',
            help="the name of the directory where the module's stub description .rst files will be placed")

    arg_parser.add_argument('--include-dir', metavar='DIR', default=[],
            action='append', dest='include_dirs',
            help="add DIR to the list of directories to search for .sip files")

    arg_parser.add_argument('--sip-file', metavar='FILE',
            help="the name of the .sip file defining the (non-stub) module")

    arg_parser.add_argument('--verbose', action='store_true', default=False,
            help="enable verbose progress messages")

    arg_parser.add_argument('modules', metavar='module', nargs=1,
            help="the fully qualified name of the module")

    args = arg_parser.parse_args()

    # Regularise the arguments.
    api = os.path.abspath(args.api)
    clean = args.clean
    descriptions = os.path.abspath(args.descriptions)
    include_dirs = [os.path.abspath(d) for d in args.include_dirs]
    sip_file = None if args.sip_file is None else os.path.abspath(args.sip_file)
    verbose = args.verbose

    parts = args.modules[0].split('.')
    package = '.'.join(parts[:-1])
    module = parts[-1]

    # Tell the user what they have specified.
    if verbose:
        print("Module description stubs will be placed in", descriptions)
        print("Module API skeletons will be placed in", api)

    # Generate the reST for the module.
    clean_skeletons(module, api, verbose)

    if clean:
        clean_descriptions(module, descriptions, verbose)

    generate_rst(module, package, descriptions, api, sip_file, include_dirs,
            verbose)
