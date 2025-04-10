# PyQt documentation build configuration file.


import datetime
import os
import sys


# The root directory of the sphinx stuff not specific to this documentation.
sphinx_root = os.path.abspath(os.path.join('..', 'sphinx'))

# Add Sphinx extension module names.
sys.path.append(os.path.join(sphinx_root, 'ext'))
extensions = ['sphinxsip', 'sphinx.ext.intersphinx']
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Add paths that contain templates here, relative to this directory.
templates_path = [os.path.join(sphinx_root, 'templates')]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyQt'
copyright = '{0}, Riverbank Computing Limited, The Qt Company'.format(
        datetime.date.today().year)

# The version info for the project, acts as replacement for |version| and
# |release|, also used in various other places throughout the built documents.
#
# The short X.Y version.
version = '6.9'
# The full version, including alpha/beta/rc tags.
release = '6.9.0'

# The number of columns in a table of class names.
sip_class_table_columns = 4

# The directory containing the descriptions.
sip_descriptions = os.path.abspath(os.path.join('..', 'descriptions'))

# The root URL for any corresponding C/C++ documentation.
sip_external_docs_root_url = 'https://doc.qt.io/qt-6'

# A list of ignored prefixes for class index sorting.
sip_ignored_class_prefixes = ['Qt', 'Q']


# -- Options for HTML output ---------------------------------------------------

# Don't include the .rst source.
html_copy_source = False

# The theme to use for HTML and HTML Help pages.
html_theme = 'riverbank'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_root]

# The name for this set of Sphinx documents.
html_title = "PyQt Documentation v{}".format(release)

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyQtdoc'
