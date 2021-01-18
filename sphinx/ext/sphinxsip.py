# Copyright (c) 2019, Riverbank Computing Limited
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


from collections import OrderedDict
import os

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import ViewList

from sphinx import addnodes
from sphinx.domains import Domain, Index, ObjType
from sphinx.errors import SphinxError
from sphinx.roles import XRefRole
from sphinx.util.nodes import nested_parse_with_titles


def parse_option_list(value):
    """ Parse a space separated list of options. """

    return None if value is None else value.strip().split()


def parse_option_multiline_list(value):
    """ Parse a newline separated list of options. """

    return None if value is None else [v.strip()
            for v in value.strip().split('\n')]


class sip_placeholder(nodes.container):
    """ A node representing a placeholder that will always be removed before
    getting to the rendering stage.
    """

    def __init__(self, name, fq_py_name=None, description=None, attr_type=None, const=None, static=None, args=None, returns=None):
        """ Initialise the object. """

        super().__init__()

        self.sip_name = name
        self.sip_fq_py_name = fq_py_name
        self.sip_description = description
        self.sip_attr_type = attr_type
        self.sip_const = const
        self.sip_static = static
        self.sip_args = args
        self.sip_returns = returns


class sip_skeleton_node(nodes.container):
    """ A skeleton-only node containing a named Python object with a
    description.
    """

    def __init__(self, description, fq_py_name):
        """ Initialise the object. """

        super().__init__()

        self.sip_description = description
        self.sip_fq_py_name = fq_py_name


class sip_attribute(sip_skeleton_node):
    """ A skeleton-only node representing a sip generated attribute. """

    def __init__(self, attr_type, const, static, *super_args):
        """ Initialise the object. """

        super().__init__(*super_args)

        self.sip_attr_type = attr_type
        self.sip_const = const
        self.sip_static = static


class sip_attribute_description(nodes.container):
    """ A node representing a description of a sip generated attribute. """

    pass


class sip_class_description(nodes.container):
    """ A node representing a description of a sip generated class. """

    def __init__(self, brief, external):
        """ Initialise the object. """

        super().__init__()

        self.sip_brief = brief
        self.sip_external = external


class sip_enum(sip_skeleton_node):
    """ A skeleton-only node representing a sip generated enum. """

    pass


class sip_enum_description(nodes.container):
    """ A node representing a description of a sip generated enum. """

    pass


class sip_enum_member(sip_skeleton_node):
    """ A skeleton-only node representing a sip generated enum member. """

    pass

class sip_enum_member_description(nodes.container):
    """ A node representing a description of a sip generated enum member. """

    def __init__(self, value):
        """ Initialise the object. """

        super().__init__()

        self.sip_value = value


class sip_method(sip_skeleton_node):
    """ A skeleton-only node representing a sip generated method. """

    def __init__(self, static, args, returns, *super_args):
        """ Initialise the object. """

        super().__init__(*super_args)

        self.sip_static = static
        self.sip_args = args
        self.sip_returns = returns


class sip_method_description(nodes.container):
    """ A node representing a description of a sip generated method. """

    pass


class sip_module_description(nodes.container):
    """ A node representing a description of a sip generated module. """

    def __init__(self, brief, platform):
        """ Initialise the object. """

        super().__init__()

        self.sip_brief = brief
        self.sip_platform = platform


class sip_signal(sip_skeleton_node):
    """ A skeleton-only node representing a sip generated signal. """

    def __init__(self, args, *super_args):
        """ Initialise the object. """

        super().__init__(*super_args)

        self.sip_args = args


class sip_signal_description(nodes.container):
    """ A node representing a description of a sip generated signal. """

    pass


class sip_decorator(nodes.literal):
    """ A skeleton-only node containing a decorator. """

    pass


class sip_declaration(addnodes.desc_signature):
    """ A skeleton-only node containing the declaration of a Python object. """

    pass


class sip_type(addnodes.desc_parameter):
    """ A skeleton-only node containing an argument or return type. """

    pass


class sip_type_list(addnodes.desc_parameterlist):
    """ A skeleton-only node containing a list of argument or return types. """

    pass


class sip_py_name(nodes.literal):
    """ A skeleton-only node containing the name of a Python object. """

    pass


class SipModuleIndex(Directive):
    """ The directive describing a list of sip generated modules. """

    def run(self):
        """ Generate the list of nodes. """

        return [sip_placeholder('module-index')]


class SipClass(Directive):
    """ The directive describing a sip generated class. """

    # The contents of the class.
    has_content = True

    # The full name of the class is required.
    required_arguments = 1

    option_spec = {
        # The file containing the class description.
        'description': lambda x: x,

        # The space separated list of fully qualified super-class names.
        'inherits': parse_option_list,

        # The phrase describing the supported platforms.
        'platform': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env
        docname = env.docname

        # Get the unique full name of the class.
        fq_py_name, py_name = get_py_name(self.arguments[0])

        # Get the super-class list and re-reST it.
        inherits = self.options.get('inherits')
        if inherits:
            superclasses = [c[c.index('`') + 2:-1] for c in inherits]
        else:
            superclasses = []

        # Save the class to create cross-references.
        xref = {
            'dispname': py_name,
            'docname':  docname,
            'anchor':   '',
            'type':     'class',
            'brief':    '',
            'inherits': superclasses,
        }

        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Get the rest of the skeleton.
        skeleton = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, skeleton)

        # Get any description.
        external = None
        description = self.options.get('description')
        if description:
            desc_container = nodes.container()

            parse_description_file(description, desc_container, self.state,
                    env)

            # Find the class description node.
            for desc_node in desc_container.traverse(sip_class_description):
                xref['brief'] = desc_node.sip_brief
                external = desc_node.sip_external
                break
        else:
            desc_container = None

        # Create the content.  We do this by creating another document that we
        # then parse.  This will create placeholders which we can then replace
        # with the real content.
        rst = ViewList()

        add_heading(rst, py_name, '=', docname)

        rst.append('', docname, 0)
        rst.append('.. sip:placeholder:: class-name', docname, 0)

        # The super-classes.
        if inherits:
            text = "    Inherits from {}.".format(", ".join(inherits))

            rst.append('', docname, 0)
            rst.append(text, docname, 0)

        # The sub-classes.
        rst.append('', docname, 0)
        rst.append('    .. sip:placeholder:: subclass-list', docname, 0)
        rst.append('        :fq_py_name: {}'.format(fq_py_name), docname, 0)

        # The platform.
        platform = self.options.get('platform')
        if platform:
            add_platform(platform, "class", rst, env)

        # The reference to external docs.
        if external:
            text = "    The C++ documentation can be found `here <{}/{}>`_.".format(
                    env.config.sip_external_docs_root_url, external)

            rst.append('', docname, 0)
            rst.append(text, docname, 0)

        # The description.
        if desc_container is not None:
            rst.append('', docname, 0)
            add_heading(rst, "Description", '-', docname)

            rst.append('', docname, 0)
            rst.append('.. sip:placeholder:: class-desc', docname, 0)

        # The nested classes.
        add_classes(fq_py_name, rst, env)

        # The enums.
        add_enums(skeleton, rst, env)

        # The attributes.
        add_attributes(skeleton, rst, env)

        # The methods.
        add_methods(skeleton, rst, env, "Methods")

        # The signals.
        need_heading = True

        for signal_node in skeleton.traverse(sip_signal):
            rst.append('', docname, 0)

            if need_heading:
                add_heading(rst, "Signals", '-', docname)
                need_heading = False
            else:
                # Use a transition to separate signals.
                rst.append('----', docname, 0)

            rst.append('', docname, 0)
            rst.append('.. sip:placeholder:: signal-name', docname, 0)
            rst.append(
                    '    :fq_py_name: {}'.format(signal_node.sip_fq_py_name),
                    docname, 0)
            rst.append(
                    '    :description: {}'.format(signal_node.sip_description),
                    docname, 0)

            if signal_node.sip_args:
                rst.append('    :args:', docname, 0)
                for arg in signal_node.sip_args:
                    rst.append('        {}'.format(arg), docname, 0)

        # Create the content, with placeholders, in a temporary container.
        container = nodes.container()
        nested_parse_with_titles(self.state, rst, container)

        # Replace the placeholders.
        previous_name = ''

        for ph in container.traverse(sip_placeholder):
            if ph.sip_name == 'attribute-name':
                replace_attribute(ph, self.state, env)

            elif ph.sip_name == 'class-name':
                desc, desc_content = declaration(env, fq_py_name, 'class',
                        include_scope=True)

                desc_content.extend(ph.children)
                ph.replace_self(desc)

            elif ph.sip_name == 'class-desc':
                replace_description(ph, desc_container)

            elif ph.sip_name == 'enum-name':
                replace_enum(ph, self.state, env)

            elif ph.sip_name == 'method-name':
                previous_name = replace_method(ph, self.state, env,
                        previous_name)

            elif ph.sip_name == 'signal-name':
                # Populate the parameter list.
                parameters = sip_type_list()

                if ph.sip_args:
                    for arg in ph.sip_args:
                        parameters.append(parse_type_hint(arg, env))

                if previous_name != ph.sip_fq_py_name:
                    anchor = env.domaindata['sip']['objects'][ph.sip_fq_py_name]['anchor']
                else:
                    anchor = None

                desc, desc_content = declaration(env, ph.sip_fq_py_name,
                        'signal', anchor=anchor, parameters=parameters)
                previous_name = ph.sip_fq_py_name

                parse_description_file(ph.sip_description, desc_content,
                        self.state, env)

                ph.replace_self(desc)

        # Return the real content.
        return container.children


class SipClassDescription(Directive):
    """ The directive describing the description of a sip generated class. """

    # The description of the class.
    has_content = True

    option_spec = {
        # The phrase describing the class.
        'brief': lambda x: x,

        # The digest of the original documentation.
        'digest': lambda x: x,

        # The relative link to any external documentation.
        'external': lambda x: x,

        # The real name of the class.
        'realname': lambda x: x,

        # The status of the description.
        'status': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Create the content.
        container = sip_class_description(self.options.get('brief', ''),
                self.options.get('external'))

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipAttribute(Directive):
    """ The directive describing a sip generated attribute. """

    # The full name of the attribute is required.
    required_arguments = 1

    option_spec = {
        # The file containing the attribute description.
        'description': lambda v: v,

        # The type hint of the attribute.
        'type': lambda v: v,

        # Set if the attribute is read-only.
        'const': lambda v: True,

        # Set if the attribute is a class attribute.
        'static': lambda v: True,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Get the unique full name of the attribute.
        fq_py_name, py_name = get_py_name(self.arguments[0])

        # Save the attribute to create cross-references.
        xref = {
            'dispname': py_name,
            'docname':  env.docname,
            'anchor':   py_name,
            'type':     'attribute',
        }

        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Create the (skeleton) content.
        return [sip_attribute(self.options.get('type'),
                self.options.get('const'), self.options.get('static'),
                self.options.get('description'), fq_py_name)]


class SipAttributeDescription(Directive):
    """ The directive describing the description of a sip generated attribute.
    """

    # The description of the attribute.
    has_content = True

    option_spec = {
        # The status of the description.
        'status': lambda x: x,

        # The digest of the original documentation.
        'digest': lambda x: x,

        # The real name of the attribute.
        'realname': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        # Create the content.
        container = sip_attribute_description()

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipEnum(Directive):
    """ The directive describing a sip generated enum. """

    # The members of the enum.
    has_content = True

    # The full name of the enum is required.
    required_arguments = 1

    option_spec = {
        # The file containing the enum description.
        'description': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Get the unique full name of the enum.
        fq_py_name, py_name = get_py_name(self.arguments[0])

        # Save the enum to create cross-references.
        xref = {
            'dispname': py_name,
            'docname':  env.docname,
            'anchor':   py_name,
            'type':     'enum',
        }

        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Create the (skeleton) content.
        enum = sip_enum(self.options.get('description'), fq_py_name)

        self.state.nested_parse(self.content, self.content_offset, enum)

        return [enum]


class SipEnumDescription(Directive):
    """ The directive describing the description of a sip generated enum. """

    # The description of the class.
    has_content = True

    option_spec = {
        # The status of the description.
        'status': lambda x: x,

        # The digest of the original documentation.
        'digest': lambda x: x,

        # The real name of the enum.
        'realname': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        # Create the content.
        container = sip_enum_description()

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipEnumMember(Directive):
    """ The directive describing a sip generated enum member. """

    # The full name of the enum member is required.
    required_arguments = 1

    option_spec = {
        # The file containing the enum member description.
        'description': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Get the unique full name of the enum member and the name of the enum.
        fq_py_name = self.arguments[0].strip()
        parts = fq_py_name.split('.')
        py_name = parts[-1]
        enum_name = parts[-2]

        # Save the enum member to create cross-references.
        xref = {
            'dispname': py_name,
            'docname':  env.docname,
            'anchor':   enum_name + '-' + py_name,
            'type':     'member',
        }

        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Create the (skeleton) content.
        return [sip_enum_member(self.options.get('description'), fq_py_name)]


class SipEnumMemberDescription(Directive):
    """ The directive describing a sip generated enum member. """

    # The description of the enum member.
    has_content = True

    option_spec = {
        # The status of the description.
        'status': lambda x: x,

        # The digest of the original documentation.
        'digest': lambda x: x,

        # The optional real name of the enum member.
        'realname': lambda x: x,

        # The optional value of the enum member.
        'value': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Create the content.
        container = sip_enum_member_description(self.options.get('value', ''))

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipMethod(Directive):
    """ The directive describing a sip generated method. """

    # The full name of the method is required.
    required_arguments = 1

    option_spec = {
        # The file containing the method description.
        'description': lambda v: v,

        # The arguments.
        'args': parse_option_multiline_list,

        # The returns.
        'returns': parse_option_multiline_list,

        # Set if the method is static.
        'static': lambda v: True,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Get the unique full name of the method.
        fq_py_name, py_name = get_py_name(self.arguments[0])

        # Save the method to create cross-references.
        xref = {
            'dispname': py_name,
            'docname':  env.docname,
            'anchor':   py_name,
            'type':     'method',
        }

        # Note that this will replace any previous overload (but with the same
        # data).
        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Create the (skeleton) content.
        return [sip_method(self.options.get('static', False),
                self.options.get('args'), self.options.get('returns'),
                self.options.get('description'), fq_py_name)]


class SipMethodDescription(Directive):
    """ The directive describing the description of a sip generated method. """

    # The description of the method.
    has_content = True

    option_spec = {
        # The status of the description.
        'status': lambda x: x,

        # The digest of the original documentation.
        'digest': lambda x: x,

        # The Python signature of the method.
        'pysig': lambda x: x,

        # The real name of the method.
        'realname': lambda x: x,

        # The real signature of the method.
        'realsig': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        # Create the content.
        container = sip_method_description()

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipSignal(Directive):
    """ The directive describing a sip generated signal. """

    # The full name of the signal is required.
    required_arguments = 1

    option_spec = {
        # The file containing the signal description.
        'description': lambda v: v,

        # The arguments.
        'args': parse_option_multiline_list,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Get the unique full name of the signal.
        fq_py_name, py_name = get_py_name(self.arguments[0])

        # Save the signal to create cross-references.
        xref = {
            'dispname': py_name,
            'docname':  env.docname,
            'anchor':   py_name,
            'type':     'signal',
        }

        # Note that this will replace any previous overload (but with the same
        # data).
        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Create the (skeleton) content.
        return [sip_signal(self.options.get('args'),
                self.options.get('description'), fq_py_name)]


class SipSignalDescription(Directive):
    """ The directive describing the description of a sip generated signal. """

    # The description of the signal.
    has_content = True

    option_spec = {
        # The status of the description.
        'status': lambda x: x,

        # The digest of the original documentation.
        'digest': lambda x: x,

        # The Python signature of the signal.
        'pysig': lambda x: x,

        # The real name of the signal.
        'realname': lambda x: x,

        # The real signature of the signal.
        'realsig': lambda x: x,
    }

    def run(self):
        """ Generate the list of nodes. """

        # Create the content.
        container = sip_signal_description()

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipModule(Directive):
    """ The directive describing a sip generated module. """

    # The contents of the module.
    has_content = True

    # The full name of the module is required.
    required_arguments = 1

    option_spec = {
        # The file containing the module description.
        'description': lambda v: v,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Get the unique full name of the module.
        fq_py_name, py_name = get_py_name(self.arguments[0])

        # Save the module to create the module index later.
        xref = {
            'dispname': py_name,
            'docname':  env.docname,
            'anchor':   '',
            'type':     'module',
            'brief':    '',
        }

        env.domaindata['sip']['objects'][fq_py_name] = xref

        # Get the rest of the skeleton.
        skeleton = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, skeleton)

        # Get any description.
        platform = None
        description = self.options.get('description')
        if description:
            desc_container = nodes.container()

            parse_description_file(description, desc_container, self.state,
                    env)

            # Find the module description node.
            for desc_node in desc_container.traverse(sip_module_description):
                xref['brief'] = desc_node.sip_brief
                platform = desc_node.sip_platform
                break
        else:
            desc_container = None

        # Create the content.  We do this by creating another document that we
        # then parse.  This will create placeholders which we can then replace
        # with the real content.
        rst = ViewList()

        add_heading(rst, py_name, '=', env.docname)

        # The platform.
        if platform:
            add_platform(platform, "module", rst, env)

        # The description.
        if desc_container is not None:
            rst.append('', env.docname, 0)
            rst.append('.. sip:placeholder:: module-desc', env.docname, 0)

        # The classes.
        add_classes(fq_py_name, rst, env)

        # The enums.
        add_enums(skeleton, rst, env)

        # The attributes.
        add_attributes(skeleton, rst, env)

        # The methods.
        add_methods(skeleton, rst, env, "Functions")

        # Create the content, with placeholders, in a temporary container.
        container = nodes.container()
        nested_parse_with_titles(self.state, rst, container)

        # Replace the placeholders.
        previous_name = ''

        for ph in container.traverse(sip_placeholder):
            if ph.sip_name == 'attribute-name':
                replace_attribute(ph, self.state, env)

            elif ph.sip_name == 'enum-name':
                replace_enum(ph, self.state, env)

            elif ph.sip_name == 'method-name':
                previous_name = replace_method(ph, self.state, env,
                        previous_name)

            elif ph.sip_name == 'module-desc':
                replace_description(ph, desc_container)

        # Return the real content.
        return container.children


class SipModuleDescription(Directive):
    """ The directive describing the description of a sip generated module. """

    # The description of the class.
    has_content = True

    option_spec = {
        # The phrase describing the class.
        'brief': lambda v: v,

        # The optional phrase describing the platform.
        'platform': lambda v: v,

        # The status of the description.
        'status': lambda v: v,
    }

    def run(self):
        """ Generate the list of nodes. """

        env = self.state.document.settings.env

        # Create the content.
        container = sip_module_description(self.options.get('brief', ''),
                self.options.get('platform'))

        nested_parse_with_titles(self.state, self.content, container)

        return [container]


class SipPlaceholder(Directive):
    """ This is an internal directive used to create a named placeholder that
    will be replaced by real content later on.
    """

    # The contents of the placeholder.
    has_content = True

    # The type of the placeholder is required.
    required_arguments = 1

    option_spec = {
        # The optional fully qualified Python name.
        'fq_py_name': lambda v: v,

        # The optional description filename.
        'description': lambda v: v,

        # The arguments (methods and signals only).
        'args': parse_option_multiline_list,

        # The returns (methods only).
        'returns': parse_option_multiline_list,

        # The optional attribute type (attributes only).
        'type': lambda v: v,

        # The optional read-only flag (attributes only).
        'const': lambda v: True,

        # The optional static flag (methods and attributes only).
        'static': lambda v: True,
    }

    def run(self):
        """ Generate the list of nodes. """

        placeholder = sip_placeholder(self.arguments[0].strip(),
            self.options.get('fq_py_name'), self.options.get('description'),
            self.options.get('type', False), self.options.get('const', False),
            self.options.get('static', False), self.options.get('args'),
            self.options.get('returns'))

        nested_parse_with_titles(self.state, self.content, placeholder)

        return [placeholder]


class SipClassIndex(Index):
    """ The class index. """

    name = 'classes'
    localname = "Class Index"
    shortname = "classes"

    def generate(self, docnames=None):
        """ Generate the index content. """

        content = OrderedDict()

        classes = [n for n, o in self.domain.data['objects'].items()
                if o['type'] == 'class']
        classes = sorted_class_names(self.domain.env, classes)

        for sort_key, fq_py_name in classes:
            letter_entries = content.setdefault(sort_key[0], [])

            # If the entry name is not unique then make sure all entries for
            # the name are disambiguated.
            dispname = self.domain.data['objects'][fq_py_name]['dispname']
            extra = ''
            for le in letter_entries:
                le_name, le_extra = le

                if self.domain.data['objects'][le_name]['dispname'] == dispname:
                    if le_extra == '':
                        le[1] = '.'.join(le_name.split('.')[:-1])

                    if extra == '':
                        extra = '.'.join(fq_py_name.split('.')[:-1])

            entry = [fq_py_name, extra]
            letter_entries.append(entry)

        # Now ambiguities are resolved we return the full entries.
        for entries in content.values():
            # Copy the list of entries and empty the original list.
            le_entries = list(entries)
            del entries[:]

            for fq_py_name, extra in le_entries:
                xref = self.domain.data['objects'][fq_py_name]
                entry = [xref['dispname'], 0, xref['docname'], '', extra, '',
                        xref['brief']]
                entries.append(entry)

        return content.items(), False


class SipXRefRole(XRefRole):
    """ A role that can be cross-referenced. """

    def process_link(self, env, refnode, has_explicit_title, title, target):
        """Process a parsed link. """

        # Fix any implicit title.
        if not has_explicit_title:
            if title.startswith('~'):
                title = title[1:]

                dot = title.rfind('.')
                if dot >= 0:
                    title = title[dot + 1:]

        return title, target


class SipDomain(Domain):
    """ Implement the sip domain. """

    name = 'sip'
    label = "sip"

    object_types = {
        'attribute':    ObjType('attribute', 'ref'),
        'class':        ObjType('class', 'ref'),
        'enum':         ObjType('enum', 'ref'),
        'member':       ObjType('member', 'ref'),
        'method':       ObjType('method', 'ref'),
        'module':       ObjType('module', 'ref'),
        'signal':       ObjType('signal', 'ref'),
    }

    directives = {
        # These are user written directives used in the main documentation.
        'module-index':             SipModuleIndex,

        # These are user written directives used in the description .rst files.
        'attribute-description':    SipAttributeDescription,
        'class-description':        SipClassDescription,
        'enum-description':         SipEnumDescription,
        'enum-member-description':  SipEnumMemberDescription,
        'method-description':       SipMethodDescription,
        'module-description':       SipModuleDescription,
        'signal-description':       SipSignalDescription,

        # These are structural directives used in the API .rst files generated
        # by sip2rst.py.
        'attribute':                SipAttribute,
        'class':                    SipClass,
        'enum':                     SipEnum,
        'enum-member':              SipEnumMember,
        'method':                   SipMethod,
        'module':                   SipModule,
        'signal':                   SipSignal,

        # These are internal directives that only appear in transient .rst
        # 'files'.
        'placeholder':              SipPlaceholder,
    }

    roles = {
        'ref':      SipXRefRole(innernodeclass=sip_py_name),
    }

    initial_data = {
        'objects':  {},
    }

    indices = [SipClassIndex]

    def clear_doc(self, docname):
        """ Clear entries related to a particular document. """

        for name, obj in list(self.data['objects'].items()):
            if obj['docname'] == docname:
                del self.data['objects'][name]

    def get_objects(self):
        """ Get the object descriptions. """

        for name, xref in self.data['objects'].items():
            anchor = xref['anchor']
            if anchor:
                anchor = '#' + anchor

            yield (name, xref['dispname'], xref['type'], xref['docname'],
                    anchor, 0)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        """ Resolve cross-references to domain-specific objects. """

        name = target[1:] if target.startswith('~') else target

        xref = env.domaindata['sip']['objects'].get(name)
        if xref is None:
            return None

        return reference_node(env.app, xref, fromdocname, child=contnode)


def sorted_class_names(env, names):
    """ Return a sorted sequence of 2-tuples of sort key and class name. """

    name_tups = []

    for name in names:
        display_name = name.split('.')[-1]

        for prefix in env.config.sip_ignored_class_prefixes:
            if display_name.startswith(prefix):
                sort_key = display_name[len(prefix):]
                if sort_key:
                    break
        else:
            sort_key = display_name

        name_tups.append((sort_key.upper(), name))

    return sorted(name_tups)


def replace_placeholders(app, doctree, fromdocname):
    """ Generate any module index in a document. """

    env = app.builder.env

    for ph in doctree.traverse(sip_placeholder):
        if ph.sip_name == 'module-index':
            replace_module_index(ph, app, fromdocname)

        elif ph.sip_name == 'subclass-list':
            replace_subclass_list(ph, app, fromdocname)

        elif ph.sip_name == 'class-table':
            replace_class_table(ph, app, fromdocname)


def replace_module_index(ph, app, fromdocname):
    """ Replace a module index placeholder. """

    env = app.builder.env

    table = nodes.table()

    group = nodes.tgroup(cols=2)
    group.append(nodes.colspec(colwidth=0.3))
    group.append(nodes.colspec(colwidth=0.7))
    table.append(group)

    body = nodes.tbody()
    group.append(body)

    for name in sorted(env.domaindata['sip']['objects'].keys()):
        xref = env.domaindata['sip']['objects'][name]
        if xref['type'] != 'module':
            continue

        # Add the new row.
        row_node = nodes.row()
        body.append(row_node)

        # Add the reference to the module page.
        row_node.append(reference_cell_node(app, xref, fromdocname))

        # Add the brief description.
        mod_brief = xref['brief']

        brief_node = nodes.Text(mod_brief, mod_brief)

        brief_para_node = nodes.paragraph()
        brief_para_node.append(brief_node)

        brief_cell_node = nodes.entry()
        brief_cell_node.append(brief_para_node)
        row_node.append(brief_cell_node)

    ph.replace_self([table])


def replace_subclass_list(ph, app, fromdocname):
    """ Replace a sub-class list placeholder. """

    env = app.builder.env
    object_map = env.domaindata['sip']['objects']

    # Find all the sub-classes that directly inherit this one.
    classes = [n for n, o in object_map.items()
            if o['type'] == 'class' and ph.sip_fq_py_name in o['inherits']]
    nr_classes = len(classes)

    # Handle the trivial case.
    if nr_classes == 0:
        # Remove the placeholder.
        ph.parent.remove(ph)

        return

    # Get the sorted class names.
    classes = [n for _, n in sorted_class_names(env, classes)]

    # Construct the paragraph.
    para = nodes.paragraph()

    prefix = "Inherited by "

    for name in classes:
        para.append(nodes.Text(prefix, prefix))
        prefix = ', '

        para.append(reference_node(app, object_map[name], fromdocname))

    para.append(nodes.Text('.', '.'))

    ph.replace_self([para])


def replace_class_table(ph, app, fromdocname):
    """ Replace a class table placeholder. """

    nr_cols = app.builder.env.config.sip_class_table_columns

    env = app.builder.env
    object_map = env.domaindata['sip']['objects']

    # Find all the scope-level classes.
    prefix = ph.sip_fq_py_name + '.'
    prefix_len = len(prefix)
    classes = [n for n, o in object_map.items()
            if o['type'] == 'class' and n.startswith(prefix) and '.' not in n[prefix_len:]]
    nr_classes = len(classes)

    # Handle the trivial case.
    if nr_classes == 0:
        # Remove the empty section.
        ph.parent.parent.remove(ph.parent)

        # Remove the corresponding entry in the sidebar TOC.
        for entry in env.tocs[fromdocname].traverse(nodes.reference):
            if entry['anchorname'] == '#classes':
                list_item = entry.parent.parent
                list_item.parent.remove(list_item)
                break

        return

    # Get the sorted class names.
    classes = [n for _, n in sorted_class_names(env, classes)]

    # Calculate the number of rows.
    nr_rows = (nr_classes + nr_cols - 1) // nr_cols

    # For small modules it looks better if we impose a minimum number of rows.
    if nr_rows < nr_cols:
        nr_rows = min(nr_cols, nr_classes)

    # Create the table.
    table = nodes.table()
    table['classes'].append('colwidths-auto')

    group = nodes.tgroup(cols=nr_cols)

    for c in range(nr_cols):
        group.append(nodes.colspec())

    table.append(group)

    body = nodes.tbody()
    group.append(body)

    for r in range(nr_rows):
        # Add the new row.
        row_node = nodes.row()
        body.append(row_node)

        for c in range(nr_cols):
            i = c * nr_rows + r
            if i < nr_classes:
                xref = object_map[classes[i]]
                row_node.append(reference_cell_node(app, xref, fromdocname))

    ph.replace_self([table])


def add_heading(rst, heading, ou_ch, docname):
    """ Add a heading to a node. """

    ou_line = ou_ch * len(heading)

    rst.append(ou_line, docname, 0)
    rst.append(heading, docname, 0)
    rst.append(ou_line, docname, 0)


def declaration(env, fq_py_name, obj_type, include_scope=False, anchor=None, decorator='', parameters=None, returns=None, attr_type=None):
    """ Return a 2-tuple of the root node containing the name and target of the
    declaration of a Python object, and the node to which subsequent content
    should be added to.
    """

    parts = fq_py_name.split('.')
    py_scope_name = '.'.join(parts[:-1])
    py_name = parts[-1]

    desc = addnodes.desc()

    # This determines the HTML class of the description list.
    desc['objtype'] = obj_type

    declaration = sip_declaration()
    desc.append(declaration)

    if anchor:
        declaration['ids'].append(anchor)

    if decorator:
        declaration.append(sip_decorator(text=decorator))

    if include_scope:
        declaration.append(pending_reference_node(env, py_scope_name))
        name_suffix = '.' + py_name
    else:
        name_suffix = py_name

    declaration.append(sip_py_name(name_suffix, name_suffix))

    if attr_type is not None:
        sep = ': '
        declaration.append(sip_py_name(sep, sep))
        declaration.append(attr_type)

    if parameters is not None:
        declaration.append(parameters)

    if returns:
        declaration.append(addnodes.desc_returns())
        declaration.append(returns)

    desc_content = addnodes.desc_content()
    desc.append(desc_content)

    return desc, desc_content


def add_attributes(skeleton, rst, env):
    """ Add the attributes from a skeleton as reST. """

    need_heading = True

    for attr_node in skeleton.traverse(sip_attribute):
        rst.append('', env.docname, 0)

        if need_heading:
            add_heading(rst, "Attributes", '-', env.docname)
            need_heading = False
        else:
            # Use a transition to separate attributes.
            rst.append('----', env.docname, 0)

        rst.append('', env.docname, 0)
        rst.append('.. sip:placeholder:: attribute-name', env.docname, 0)
        rst.append('    :fq_py_name: {}'.format(attr_node.sip_fq_py_name),
                env.docname, 0)
        rst.append('    :description: {}'.format(attr_node.sip_description),
                env.docname, 0)

        rst.append('    :type: {}'.format(attr_node.sip_attr_type),
                env.docname, 0)

        if attr_node.sip_const:
            rst.append('    :const:', env.docname, 0)

        if attr_node.sip_static:
            rst.append('    :static:', env.docname, 0)


def add_classes(fq_scope_name, rst, env):
    """ Add a table of classes contained in a scope as a placeholder. """

    rst.append('', env.docname, 0)
    add_heading(rst, "Classes", '-', env.docname)
    rst.append('', env.docname, 0)
    rst.append('.. sip:placeholder:: class-table', env.docname, 0)
    rst.append('    :fq_py_name: {}'.format(fq_scope_name), env.docname, 0)


def add_enums(skeleton, rst, env):
    """ Add the enums from a skeleton as reST. """

    need_heading = True

    for enum_node in skeleton.traverse(sip_enum):
        rst.append('', env.docname, 0)

        if need_heading:
            add_heading(rst, "Enums", '-', env.docname)
            need_heading = False
        else:
            # Use a transition to separate enums.
            rst.append('----', env.docname, 0)

        rst.append('', env.docname, 0)
        rst.append('.. sip:placeholder:: enum-name', env.docname, 0)
        rst.append('    :fq_py_name: {}'.format(enum_node.sip_fq_py_name),
                env.docname, 0)
        rst.append('    :description: {}'.format(enum_node.sip_description),
                env.docname, 0)

        for member_node in enum_node.traverse(sip_enum_member):
            rst.append('', env.docname, 0)
            rst.append('    .. sip:placeholder:: enum-member', env.docname, 0)
            rst.append(
                    '        :fq_py_name: {}'.format(
                            member_node.sip_fq_py_name),
                    env.docname, 0)
            rst.append(
                    '        :description: {}'.format(
                            member_node.sip_description),
                    env.docname, 0)


def add_methods(skeleton, rst, env, title):
    """ Add the methods/functions from a skeleton as reST. """

    need_heading = True

    for method_node in skeleton.traverse(sip_method):
        rst.append('', env.docname, 0)

        if need_heading:
            add_heading(rst, title, '-', env.docname)
            need_heading = False
        else:
            # Use a transition to separate methods.
            rst.append('----', env.docname, 0)

        rst.append('', env.docname, 0)
        rst.append('.. sip:placeholder:: method-name', env.docname, 0)
        rst.append('    :fq_py_name: {}'.format(method_node.sip_fq_py_name),
                env.docname, 0)
        rst.append('    :description: {}'.format(method_node.sip_description),
                env.docname, 0)

        if method_node.sip_args:
            rst.append('    :args:', env.docname, 0)
            for arg in method_node.sip_args:
                rst.append('        {}'.format(arg), env.docname, 0)

        if method_node.sip_returns:
            rst.append('    :returns:', env.docname, 0)
            for ret in method_node.sip_returns:
                rst.append('        {}'.format(ret), env.docname, 0)

        if method_node.sip_static:
            rst.append('    :static:', env.docname, 0)


def add_platform(platform, type_name, rst, env):
    """ Add the platform-specific details for an object as reST. """

    rst.append('', env.docname, 0)
    rst.append("The {} is only available on {}.".format(type_name, platform),
            env.docname, 0)


def replace_attribute(ph, state, env):
    """ Replace an attribute placeholder. """

    desc, desc_content = declaration(env, ph.sip_fq_py_name, 'attribute',
            attr_type=parse_type_hint(ph.sip_attr_type, env))

    if ph.sip_const:
        if ph.sip_static:
            detail = "This is a read-only class attribute."
        else:
            detail = "This is a read-only attribute."
    elif ph.sip_static:
        detail = "This is a class attribute."
    else:
        detail = None

    if detail:
        para = nodes.paragraph()
        desc_content.append(para)

        para.append(nodes.Text(detail, detail))

    parse_description_file(ph.sip_description, desc_content, state, env)
    ph.replace_self(desc)


def replace_description(ph, desc_container):
    """ Replace a description placeholder. """

    ph.replace_self(desc_container.children)


def replace_enum(ph, state, env):
    """ Replace an enum placeholder. """

    object_map = env.domaindata['sip']['objects']

    # Handle the enum description.
    desc, desc_content = declaration(env, ph.sip_fq_py_name, 'enum',
            anchor=object_map[ph.sip_fq_py_name]['anchor'])
    parse_description_file(ph.sip_description, desc_content, state, env)

    # Parse each enum member description.
    rows = []
    nr_cols = 2

    for member_ph in ph:
        assert member_ph.sip_name == 'enum-member'

        xref = object_map[member_ph.sip_fq_py_name]

        # The member is rendered as a table row.
        row = nodes.row()

        # Parse the optional description.
        desc_td = nodes.entry()
        parse_description_file(member_ph.sip_description, desc_td, state, env)

        # Find the enum member description node.
        for desc_node in desc_td.traverse(sip_enum_member_description):
            value = desc_node.sip_value

        # The member column.
        td = nodes.entry()
        row.append(td)
        td['ids'].append(xref['anchor'])
        py_name = xref['dispname']
        cell = sip_py_name(py_name, py_name)
        td.append(cell)

        # The value column.
        td = nodes.entry()
        row.append(td)
        cell = nodes.paragraph(text=value)
        td.append(cell)

        # Only add the description column if it is needed.
        if len(desc_td) != 0:
            row.append(desc_td)
            nr_cols = 3

        rows.append(row)

    # Create the table of the enum members.
    table = nodes.table()
    table['classes'].extend(['sip-enum-table', 'colwidths-auto'])
    desc_content.append(table)

    group = nodes.tgroup(cols=nr_cols)
    table.append(group)

    for c in range(nr_cols):
        group.append(nodes.colspec())

    thead = nodes.thead()
    group.append(thead)

    thead_row = nodes.row()
    thead.append(thead_row)

    headings = ("Member", "Value", "Description")

    for c in range(nr_cols):
        th = nodes.entry()
        thead_row.append(th)
        para = nodes.paragraph(text=headings[c])
        th.append(para)

    # Add the body.
    body = nodes.tbody()
    group.append(body)
    body.extend(rows)

    ph.replace_self(desc)


def replace_method(ph, state, env, previous_name):
    """ Replace a method/function placeholder. """

    # Populate the parameter list.
    parameters = sip_type_list()

    if ph.sip_args:
        for arg in ph.sip_args:
            parameters.append(parse_type_hint(arg, env))

    # Populate the result list.
    if ph.sip_returns:
        if len(ph.sip_returns) > 1:
            returns = sip_type_list()

            for ret in ph.sip_returns:
                returns.append(parse_type_hint(ret, env))
        else:
            returns = parse_type_hint(ph.sip_returns[0], env)
    else:
        returns = None

    decorator = '@staticmethod' if ph.sip_static else ''

    if previous_name != ph.sip_fq_py_name:
        anchor = env.domaindata['sip']['objects'][ph.sip_fq_py_name]['anchor']
    else:
        anchor = None

    desc, desc_content = declaration(env, ph.sip_fq_py_name, 'method',
            anchor=anchor, decorator=decorator, parameters=parameters,
            returns=returns)

    parse_description_file(ph.sip_description, desc_content, state, env)
    ph.replace_self(desc)

    return ph.sip_fq_py_name


def reference_node(app, xref, fromdocname, child=None):
    """ Create a new reference node for an object. """

    docname = xref['docname']
    anchor = xref['anchor']

    if anchor:
        anchor = '#' + anchor

    ref_node = nodes.reference()
    ref_node['refdocname'] = docname
    ref_node['refuri'] = app.builder.get_relative_uri(fromdocname, docname) + anchor

    if child is None:
        dispname = xref['dispname']
    else:
        # Copy the existing text.
        dispname = str(child.children[0])

    # Add parentheses if the object is a method.  The usual way of doing this
    # is to have a different role but we want to use a generic role for all
    # object types.
    if xref['type'] == 'method':
        dispname += '()'

    ref_node.append(sip_py_name(dispname, dispname))

    return ref_node


def reference_cell_node(app, xref, fromdocname):
    """ Create a table cell node caintaining a reference to an object. """

    ref_node = reference_node(app, xref, fromdocname)

    ref_para_node = nodes.paragraph()
    ref_para_node.append(ref_node)

    ref_cell_node = nodes.entry()
    ref_cell_node.append(ref_para_node)

    return ref_cell_node


def pending_reference_node(env, name, role='ref', domain='sip'):
    """ Create a pending reference for a name. """

    # Get the name that will be displayed.
    if name.startswith('~'):
        name = name[1:]
        dispname = name.split('.')[-1]
    else:
        dispname = name

    pxref = addnodes.pending_xref()

    pxref['refdoc'] = env.docname
    pxref['refdomain'] = domain
    pxref['reftype'] = role
    pxref['reftarget'] = name

    pxref.append(sip_py_name(dispname, dispname))

    return pxref


def parse_description_file(description, container, state, env):
    """ Parse a description file into a container node. """

    # Convert to an absolute pathname.
    description = os.path.join(env.config.sip_descriptions, description)

    # Populate a view list.
    rst = ViewList()
    line_nr = 1

    with open(description, 'rt') as df:
        line = df.readline()
        while line:
            rst.append(line.rstrip(), description, line_nr)
            line_nr += 1
            line = df.readline()

    # Parse the view list.
    nested_parse_with_titles(state, rst, container)


def get_py_name(raw):
    """ Return a 2-tuple of a fully qualified name of a Python object and its
    basename.
    """

    fq_py_name = raw.strip()
    py_name = fq_py_name.split('.')[-1]

    return fq_py_name, py_name


def parse_type_hint(type_hint, env):
    """ Parse a type hint and return the corresponding type node. """

    type_node = sip_type()

    ref_start = find_ref_start(type_hint)
    while ref_start >= 0:
        # Add any leading text:
        if ref_start > 0:
            leading = type_hint[:ref_start]
            type_node.append(sip_py_name(leading, leading))
            type_hint = type_hint[ref_start:]

        # Find the end of the reference, i.e. the second backtick.
        first = type_hint.find('`')
        if first < 0:
            break

        second = type_hint[first + 1:].find('`')
        if second < 0:
            break

        # The start of any trailing text.
        trailing = first + second + 2

        # Extract and parse the reference.
        parse_rest_reference(type_hint[:trailing], type_node, env)

        # Remove the reference.
        type_hint = type_hint[trailing:]

        # Find the next reference.
        ref_start = find_ref_start(type_hint)

    # Add any trailing text.
    if type_hint:
        type_node.append(sip_py_name(type_hint, type_hint))

    return type_node


def find_ref_start(ref):
    """ Find the start of a reST reference in a string. """

    offset = 0
    colon = ref.find(':')
    while colon >= 0:
        if colon + 1 == len(ref):
            return -1

        # If there is a space after the colon then this is likely to be the
        # argument name rather than a reference.
        if ref[colon + 1] != ' ':
            return offset + colon

        ref = ref[colon + 2:]
        offset += colon + 2
        colon = ref.find(':')

    return -1


def parse_rest_reference(ref, type_node, env):
    """ Parse a reST reference and add it to a type node. """

    # Break the reference into its component parts.
    parts = ref[1:].split(':')

    if len(parts) != 3 or not parts[2].startswith('`') or not parts[2].endswith('`'):
        raise SphinxError("invalid reference '{}'".format(ref))

    domain, role, name = parts
    name = name[1:-1]

    type_node.append(
            pending_reference_node(env, name, role=role, domain=domain))


def noop(self, node):
    """ A no-op for node visitors. """

    pass


def depart_decorator(self, node):
    """ Depart a decorator node. """

    self.body.append('<br />')


def visit_declaration(self, node):
    """ Visit a declaration node. """

    self.body.append(self.starttag(node, 'dt', CLASS='sip-declaration'))


def depart_declaration(self, node):
    """ Depart a declaration node. """

    self.body.append('</dt>')


def visit_type(self, node):
    """ Visit a type node. """

    if isinstance(node.parent, sip_type_list):
        if node.parent.sip_need_comma:
            self.body.append(", ")
        else:
            node.parent.sip_need_comma = True


def visit_type_list(self, node):
    """ Visit a type list node. """

    node.sip_need_comma = False
    self.body.append('(')


def depart_type_list(self, node):
    """ Depart a type list node. """

    self.body.append(')')


def setup(app):
    """ The setup function for the extension that adds the additional features
    needed by documentation for sip generated modules.
    """

    app.add_config_value('sip_class_table_columns', 4, 'html')
    app.add_config_value('sip_descriptions', 'descriptions', 'html')
    app.add_config_value('sip_external_docs_root_url', '', 'html')
    app.add_config_value('sip_ignored_class_prefixes', [], 'html')

    # Public node types.
    app.add_node(sip_attribute_description, html=(noop, noop))
    app.add_node(sip_class_description, html=(noop, noop))
    app.add_node(sip_enum_description, html=(noop, noop))
    app.add_node(sip_enum_member_description, html=(noop, noop))
    app.add_node(sip_method_description, html=(noop, noop))
    app.add_node(sip_module_description, html=(noop, noop))
    app.add_node(sip_signal_description, html=(noop, noop))

    # Private node types.
    app.add_node(sip_declaration, html=(visit_declaration, depart_declaration))
    app.add_node(sip_decorator, html=(noop, depart_decorator))
    app.add_node(sip_placeholder, html=(noop, noop))
    app.add_node(sip_py_name, html=(noop, noop))
    app.add_node(sip_type, html=(visit_type, noop))
    app.add_node(sip_type_list, html=(visit_type_list, depart_type_list))

    app.add_domain(SipDomain)

    app.connect('doctree-resolved', replace_placeholders)

    return {'version': '0.1'}
