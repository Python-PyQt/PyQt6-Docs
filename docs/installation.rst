Installing PyQt5
================

Both the GPL and commercial versions of PyQt5 can be built from source packages
or installed from binary wheels.  Although this section concentrates on PyQt5
itself it applies equally to the related projects (i.e. PyQtWebEngine, PyQt3D,
PyQtChart, PyQtDataVisualization and PyQtPurchasing).


Understanding the Correct Version to Install
--------------------------------------------

Historically the version number of PyQt bears no relation to the version of Qt
supported.  For example it wasn't even true that PyQt4 required Qt v4 as it
would also build against Qt v5.  People sometimes mistakenly believe that, for
example, PyQt5 v5.13 is needed when building against Qt v5.13.

Qt uses `semantic versioning <https://semver.org/spec/v2.0.0.html>`__ when
deciding on the version number of a release.  In summary the major version is
increased when a release includes incompatible changes, the minor version is
increased when a release includes compatible changes, and the patch version is
increased when a release includes no user-visible changes.

With PyQt5 the version number of PyQt5 is tied, to a certain extent, to the
version of Qt v5 so that:

- The major version will always be **5**.

- For a particular minor version *n* it will build against any version of Qt
  v5, but will not support any new features introduced in Qt v5.\ *n+1* or
  later.

- It will support all the features of supported modules of Qt v5.\ *n* or
  earlier.

- Support for new modules may be added to PyQt5 at any time.  This would result
  in a change of patch version only.

- The major and minor versions of the latest release of PyQt5 will be the same
  as the latest release of Qt v5.

- The patch versions of PyQt5 and Qt v5 are entirely unrelated to each other.

So, for example, PyQt5 v5.1 will build against Qt v5.2 but will not support any
new features introduced in Qt v5.2.  PyQt5 v5.1 will support all the features
of supported modules of Qt v5.0 and those new features introduced in Qt v5.1.

In summary, you should always try and use the latest version of PyQt5 no matter
what version of Qt v5 you are using.


Installing from Wheels
----------------------

Wheels are the standard Python packaging format for pure Python or binary
extension modules such as PyQt5.  Only Python v3.5 and later are supported.
Wheels are provide for 32- and 64-bit Windows, 64-bit macOS and 64-bit Linux.
These correspond with the platforms for which The Qt Company provide binary
installers.

Wheels are installed using the :program:`pip` program that is included with
current versions of Python.


Installing the GPL Version
..........................

To install the wheel for the GPL version of PyQt5, run::

    pip install PyQt5

This will install the wheel for your platform and your version of Python
(assuming both are supported).  The wheel will be automatically downloaded from
PyPI.

If you get an error message saying that no downloads could be found that
satisfy the requirement then you are probably using an unsupported version of
Python.

The PyQt5 wheel includes the necessary parts of the LGPL version of Qt.  There
is no need to install Qt yourself.  You can use the :program:`pyqt-bundle`
program to create a new wheel with a different version of Qt bundled.  See
:ref:`ref-pyqt-bundle` for the full details of how to do this.

The :sip:ref:`~PyQt5.sip` module is packaged as a separate wheel which will be
downloaded and installed automatically.

To uninstall the GPL version, run::

    pip uninstall PyQt5

.. note::
   Qt's support for TLS/SSL will not work on Windows when installing wheels
   that contain Qt v5.12.4 (or later) with Python v3.7.0 to v3.7.3.  This is
   because of incompatibilities between the different versions of OpenSSL that
   these versions require.  All other version combinations should be fine.


Installing the Commercial Version
.................................

It is not possible to provide wheels for the commercial version in the same way
they are provided for the GPL version as it is not possible to distribute a
copy of the commercial version of Qt.  Therefore the :program:`pyqt-bundle`
program must be used to bundle your own copy of Qt with the provided commercial
wheels.

.. note::

    The old Riverbank Computing website provided *unlicensed* commercial wheels
    that required you to download and run the :program:`pyqtlicense` program in
    order to create a *licensed* wheel.  The new Riverbank Computing website
    provides pre-licensed wheels and there is no need to run
    :program:`pyqtlicense`.

To uninstall the commercial version, run::

    pip uninstall PyQt5-commercial


Building and Installing from Source
-----------------------------------

Starting with PyQt5 v5.14.0 :program:`pip` can be used to download, build and
install the GPL source packages from the `PyQt5
<https://pypi.org/project/PyQt5/>`__ project at PyPI.  For this to work your
:envvar:`PATH` environment variable must contain your Qt installation's ``bin``
directory.  If you do not do this then you will get a cryptic error message
from :program:`pip`.

However using :program:`pip` to install from the source package is not
recommended as it is not possible to configure the installation or to easily
diagnose any problems.  The rest of these instructions assume that you have
downloaded the source package from PyPI and will used SIP's
:program:`sip-install` command line tool to do the build and installation.

If you are using the commercial version of PyQt5 then you should use the
download instructions which were sent to you when you made your purchase.  You
must also download your ``pyqt-commercial.sip`` license file.


Installing Prerequisites
........................

`PyQt-builder <https://pypi.org/project/PyQt-builder/>`__ extends the SIP build
system and can be installed from PyPI by running::

    pip install PyQt-builder

This will also automatically install SIP if required.

PyQt-builder extends the build system by adding `options
<https://www.riverbankcomputing.com//static/Docs/PyQt-builder/command_line_tools.html>`__
to SIP's `command line tools
<https://www.riverbankcomputing.com/static/Docs/sip/command_line_tools.html>`__.

PyQt5 further extends the build system by adding the following options to SIP's
command line tools.

.. option:: --confirm-license

    Using this confirms that you accept the terms of the PyQt5 license.  If it
    is omitted then you will be asked for confirmation during configuration.

.. option:: --dbus DIR

    The directory containing the :file:`dbus/dbus-python.h` header file of the
    dbus-python package can be found in the directory ``DIR``.

.. option:: --license-dir DIR

    The license files needed by the commercial version of PyQt5 can be found in
    the directory ``DIR``.

.. option:: --no-dbus-python

    The Qt support for the dbus-python package will not be built.

.. option:: --no-designer-plugin

    The Qt Designer plugin will not be built.

.. option:: --no-qml-plugin

    The :program:`qmlscene` plugin will not be built.

.. option:: --no-tools

    The :program:`pyuic5`, :program:`pyrcc5` and :program:`pylupdate5` tools
    will not be built.

.. option:: --qt-shared

    Normally Qt is checked to see if it has been built as shared libraries.
    Some Linux distributions configure their Qt builds to make this check
    unreliable.  This option ignores the result of the check and assumes that
    Qt has been built as shared libraries.

The Mercurial repository containing the latest development version of
PyQt-builder can be found `here
<https://www.riverbankcomputing.com/hg/PyQt-builder/>`__.


Building the :sip:ref:`~PyQt5.sip` Module
.........................................

It is not necessary to install the :sip:ref:`PyQt5.sip` module before building
PyQt5 but it must be installed before PyQt5 can be used.  

The module is built using :py:mod:`setuptools` and is available from the
`PyQt5-sip <https://pypi.org/project/PyQt5-sip/>`__ project at PyPI.  It uses
:py:mod:`setuptools` as its build system and can be installed by :program:`pip`
or you can also unpack the sdist and install it by running its
:program:`setup.py` script.


Building PyQt5
..............

Once you have downloaded the source package from PyPI, unpack it and change
directory to its top level directory (i.e. the one containing the
:file:`pyproject.toml` file.  To build and install PyQt5, run::

    sip-install

In order to see all the available command line options, run::

    sip-install -h

If you want to run :program:`make` seperately then instead run::

    sip-build --no-make
    make
    make install


Building PyQt5-related Projects
...............................

The additional PyQt5 projects (i.e. PyQtWebEngine, PyQt3D, PyQtChart,
PyQtDataVisualization and PyQtPurchasing) are built and installed in exactly
the same way as PyQt5 itself.  PyQt5 must be built and installed first.


.. _ref-pyqt-bundle:

Bundling Qt Using :program:`pyqt-bundle`
----------------------------------------

The wheels of the GPL version of PyQt5 and related projects on PyPI bundle a
copy of the relevant parts of Qt.  This is done so that users can install a
complete PyQt environment with a single :program:`pip` install.

The wheels of the commercial version of PyQt do not have a copy of Qt bundled
because it is not possible to distribute a copy of the commercial version of
Qt.  Therefore a commercial user must bundle their own copy of Qt to create a
complete wheel.

The :program:`pyqt-bundle` program is provided as a means of bundling the
relevant parts of a local Qt installation with a wheel, replacing any existing
copy.  You can also use it to produce a stripped down version of PyQt that
contains only those modules you actually want to use.  :program:`pyqt-bundle`
is part of `PyQt-builder <https://pypi.org/project/PyQt-builder/>`__ and is
documented `here
<https://www.riverbankcomputing.com//static/Docs/PyQt-builder/pyqtbundle.html>`__.
