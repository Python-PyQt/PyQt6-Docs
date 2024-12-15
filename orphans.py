# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


import os


class APICache:
    """ The implementation of a cache of the contents of API files. """

    def __init__(self, root_dir):
        """ Initialise the cache. """

        self._api_root_dir = os.path.join(root_dir, 'docs', 'api')
        self._cache = None
        self._api_dir = None

    def is_orphan(self, scope, scope_is_module, target):
        """ Return True if a target description file is an orphan. """

        # Construct the name of the API file.
        api_file = os.path.join(self._api_dir, scope.lower())

        if scope_is_module:
            api_file += '-module'

        api_file += '.rst'

        # Get the (possibly cached) contents of the API file.
        try:
            api = self._cache[api_file]
        except KeyError:
            try:
                with open(api_file) as f:
                    api = f.read()
            except FileNotFoundError:
                return True

            self._cache[api_file] = api

        return target not in api

    def set_module(self, module_name):
        """ Set the name of the current module. """

        self._api_dir = os.path.join(self._api_root_dir, module_name.lower())
        self._cache = {}


def orphans(root_dir, remove):
    """ Display and optionally remove any orphaned description files. """

    api_cache = APICache(root_dir)

    # Determine how to fully remove a description file.
    if os.path.isdir(os.path.join(root_dir, '.hg')):
        rm_command = 'hg rm'
    elif os.path.isdir(os.path.join(root_dir, '.git')):
        rm_command = 'git rm'
    else:
        rm_command = 'rm'

    for dirpath, _, filenames in os.walk(os.path.join(root_dir, 'descriptions')):
        module_name = os.path.basename(dirpath)
        api_cache.set_module(module_name)

        for fn in filenames:
            target = module_name + '/' + fn

            # Extract the scope and its type.
            parts = fn[:-4].split('-')

            if parts[-1][0].isdigit():
                parts.pop()

            type_ch = parts.pop()
            nr_parts = len(parts)

            if (nr_parts == 1 and type_ch != 'c') or (nr_parts == 2 and type_ch == 'v'):
                scope = module_name
                scope_is_module = True
            else:
                scope = parts[0]
                scope_is_module = (type_ch == 'm')

            if api_cache.is_orphan(scope, scope_is_module, target):
                desc_fn = os.path.join(dirpath, fn)

                if remove:
                    cmd = rm_command + ' ' + desc_fn
                    print(cmd)
                    os.system(cmd)
                else:
                    print(desc_fn)


if __name__ == '__main__':

    # Parse the command line.
    import argparse

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--remove', action='store_true', default=False,
            help="remove any orphaned description files")

    args = arg_parser.parse_args()

    # This script is in the root directory.
    orphans(os.path.dirname(__file__), args.remove)
