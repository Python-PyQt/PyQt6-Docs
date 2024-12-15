# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


import os


class APICache:
    """ The implementation of a cache of the contents of API files. """

    def __init__(self, root_dir):
        """ Initialise the cache. """

        self._api_root_dir = os.path.join(root_dir, 'docs', 'api')
        self._api_dir = None
        self._cache = None
        self._module_name = None

    def is_orphan(self, target_fn):
        """ Return True if a target description file is an orphan. """

        # Extract the scope.
        scope = target_fn[:-4].split('-')

        if scope[-1][0].isdigit():
            scope.pop()

        type_ch = scope.pop()

        # If the name is that of an enum member, remove it.
        if type_ch == 'v':
            scope.pop()

        # Unless it is a class, remove the name of the item (leaving the
        # scope).
        if type_ch != 'c':
            scope.pop()

        if len(scope) == 0:
            scope = [self._module_name, 'module']

        api_file = os.path.join(
                self._api_dir, '-'.join(scope).lower() + '.rst')

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

        target = self._module_name + '/' + target_fn

        return target not in api

    def set_module(self, module_name):
        """ Set the name of the current module. """

        self._api_dir = os.path.join(self._api_root_dir, module_name.lower())
        self._cache = {}
        self._module_name = module_name


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
            if api_cache.is_orphan(fn):
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
