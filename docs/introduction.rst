Introduction
============

This is the reference guide for PyQt5 v\ |version|.  PyQt5 is a set of
`Python <https://www.python.org>`__ bindings for v5 of the Qt application
framework from `The Qt Company <https://www.qt.io>`__.

Qt is a set of C++ libraries and development tools that includes platform
independent abstractions for graphical user interfaces, networking, threads,
regular expressions, SQL databases, SVG, OpenGL, XML, user and application
settings, positioning and location services, short range communications (NFC
and Bluetooth), web browsing, 3D animation, charts, 3D data visualisation and
interfacing with app stores.  PyQt5 implements over 1000 of these classes as a
set of Python modules.

PyQt5 supports the Windows, Linux, UNIX, Android, macOS and iOS platforms.

PyQt does not include a copy of Qt. You must obtain a correctly licensed copy
of Qt yourself.  However, binary wheels of the GPL version of PyQt5 are
provided and these include a copy of the appropriate parts of the LGPL version
of Qt.

The homepage for PyQt5 is https://www.riverbankcomputing.com/software/pyqt/.
Here you will always find the latest stable version, current development
previews, and the latest version of this documentation.

PyQt5 is built using the `SIP bindings generator
<https://www.riverbankcomputing.com/software/sip/>`__.  SIP must be installed
in order to build and use PyQt5.

Earlier versions of Qt are supported by PyQt4.


License
-------

PyQt5 is dual licensed on all platforms under the Riverbank Commercial License
and the GPL v3.  Your PyQt5 license must be compatible with your Qt license.
If you use the GPL version then your own code must also use a compatible
license.

PyQt5, unlike Qt, is not available under the LGPL.

You can purchase a commercial PyQt5 license `here
<https://www.riverbankcomputing.com/commercial/buy>`__.


PyQt5 Components
----------------

PyQt5 comprises a number of different components.  First of all there are a
number of Python extension modules.  These are all installed in the
``PyQt5`` Python package and are described in the
:ref:`list of modules<ref-module-index>`.

PyQt5 is distributed as a number of source packages and corresponding binary
wheels each of which implement one or more logically related extension modules.

PyQt5 contains plugins that enable Qt Designer and :program:`qmlscene` to be
extended using Python code.  See :ref:`ref-designer-plugins` and
:ref:`ref-integrating-qml` respectively for the details.

PyQt5 also contains a number of utility programs.

- :program:`pyuic5` corresponds to the Qt :program:`uic` utility.  It converts
  :sip:ref:`~PyQt5.QtWidgets` based GUIs created using Qt Designer to Python
  code.

- :program:`pyrcc5` corresponds to the Qt :program:`rcc` utility.  It embeds
  arbitrary resources (eg. icons, images, translation files) described by a
  resource collection file in a Python module.

- :program:`pylupdate5` corresponds to the Qt :program:`lupdate` utility.  It
  extracts all of the translatable strings from Python code and creates or
  updates ``.ts`` translation files.  These are then used by Qt Linguist to
  manage the translation of those strings.

The `DBus <http://www.freedesktop.org/wiki/Software/DBusBindings>`__ support
module is installed as :sip:ref:`dbus.mainloop.pyqt5`.  This module provides
support for the Qt event loop in the same way that the
:sip:ref:`dbus.mainloop.glib` included with the standard ``dbus-python``
bindings package provides support for the GLib event loop.  The API is
described in :ref:`ref-dbus`.  It is only available if the ``dbus-python``
v0.80 (or later) bindings package is installed.  The :sip:ref:`~PyQt5.QtDBus`
module provides a more Qt-like interface to DBus.

When PyQt5 is configured a file called :file:`PyQt5.api` is generated.  This
can be used by the
`QScintilla <https://www.riverbankcomputing.com/software/qscintilla/>`_
editor component to enable the use of auto-completion and call tips when
editing PyQt5 code.  The API file is installed automatically if
`QScintilla <https://www.riverbankcomputing.com/software/qscintilla/>`_
is already installed.

PyQt5 includes a large number of examples.  These are ports to Python of many
of the C++ examples provided with Qt.  They can be found in the
:file:`examples` directory.

Finally, PyQt5 contains the ``.sip`` files used by SIP to generate PyQt5
itself.  These can be used by developers of bindings of other Qt based class
libraries.
