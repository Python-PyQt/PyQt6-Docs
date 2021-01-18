Contributing to this Documentation
==================================

The reference section of this documentation describes each element of the PyQt6
API.  It is based on the original Qt documentation which, of course, contains
many references to C++.  The intention is that, over time, the documentation
will be updated to replace all of the C++ idioms with their Python equivalents.
However, given the size of the API, it is unlikely that this task will ever be
complete.

The system used to create the documentation has been designed to make it easy
for users to contribute patches converting it from C++ to Python a bit at a
time.  This is done in such as a way as to ensure that the documentation can be
updated with new releases of both PyQt6 and Qt without losing any
user-contributed modifications.

The documentation itself is written as reStructuredText and generated using
`Sphinx <https://www.sphinx-doc.org>`__.

The documentation has its own public Mercurial repository
`here <https://www.riverbankcomputing.com/hg/PyQt6-Docs>`__.  The repository
can be cloned using the following command::

    hg clone https://www.riverbankcomputing.com/hg/PyQt6-Docs

The latest version will always be on the ``default`` branch.


Repository Structure
--------------------

The ``docs`` directory contains the handwritten overview documentation.

The ``docs/api`` directory contains the stuctured skeleton of the API
documentation.  It is automatically generated from the PyQt6 ``.sip`` files and
are updated with every new release of PyQt6.  They include information on all
elements of the API, including method arguments and types, but do not contain
any descriptions of those elements.  They must not be modified by hand.

The ``descriptions`` directory contains a file for every individual element of
the PyQt6 API - even down to individual enum members.  Amongst other things,
a file contains the reStructuredText describing the API element and a
``:status:`` field describing the status of the description.  It is this
``:status:`` field than ensures that any user contributed modifications cannot
be subsequently overwritten.  Description files are initially created when a
new release of PyQt6 introduces new elements to the API.  Those description
files that haven't been modified will be overwritten with every new release of
Qt.

The ``images`` directory contains the images that are referered to in
description files.  Originally they were copied from the Qt documentation and
may be replaced by more Python-centric alternatives.

The ``snippets`` directory contains the code snippets that are referered to in
description files.  Originally they were copied from the Qt documentation but
with every line of C++ code turned into a Python comment.

The ``sphinx`` directory contains a Sphinx extension and theme that implements
the documentation system.

The ``sip2rst.py`` script is run whenever a new release of PyQt6 is made.  It
updates the ``docs/api`` and ``descriptions`` directories.

The ``webxml2rst.py`` script is run whenever a new release of Qt is made.  It
updates the ``descriptions``, ``images`` and ``snippets`` directories.

.. note::

   The naming convention used for description files requires that the
   repository is cloned to a case sensitive filesystem.


Description Files
-----------------

Most contributions to the documentation will be patches to description files.
The description files for each module are placed in a module-specific
sub-directory of ``descriptions``.  The name of a description file is derived
from the fully qualified name of the API element being described, a type tag,
an optional unique identifier, and a ``.rst`` extension.

For example the description file for the :sip:ref:`~PyQt6.QtCore.QObject` class
is ``descriptions/QtCore/QObject-c.rst``.  Here the type tag ``c`` denotes a
class.  The complete set of type tags is shown in the table below.

+---+----------------------+
| a | an attribute         |
+---+----------------------+
| c | a class              |
+---+----------------------+
| e | an enum              |
+---+----------------------+
| f | a function or method |
+---+----------------------+
| m | a module             |
+---+----------------------+
| s | a signal             |
+---+----------------------+
| v | an enum member       |
+---+----------------------+

A function, method or signal may have overloads.  Each overload is described in
a separate file.  In these cases the name of each file also includes a unique
numerical identifer.  You must look at the ``:realsig:`` field within the
description file to determine which of the overloads the file describes.

Apart from the reST description itself, the only part of the description file
that should be modified is the ``:status:`` field.  The possible values of this
field are described below.

**todo**
    The description is that extracted from the last release of Qt (or a stub if
    nothing was extracted) and has not been subsequently modified.  It will be
    replaced when the next release of Qt is made.

**done**
    The description has been modified and will not be overwritten by the next
    release of Qt.

**review**
    The description has been modified.  However the original description in the
    Qt document has itself been updated since the modifications were made.
    Therefore the changes to the Qt documentation should be reviewed to see if
    corresponding changes should be made to the description.

It follows from the above that any contributed change to a description file
should set the ``:status:`` field to ``done``.

Any other fields in a description file must not be modified.

The description itself may use any of the normal Sphinx and docutils domains,
directives and roles.  The only exception is that all cross-references to any
element of the PyQt6 API should use the ``:sip:ref`` role.  For example, a
reference to the :sip:ref:`~PyQt6.QtCore.QObject` class should be specified as
``:sip:ref:`~PyQt6.QtCore.QObject```.


Contributing Patches
--------------------

User contributed patches can cover any of the following:

- ``descriptions``
- ``docs``
- ``images``
- ``snippets``
- ``sphinx/riverbank/static/riverbank.css``.

A patch is created by using the ``hg diff`` command.  Patches should be emailed
to support@riverbankcomputing.com.
