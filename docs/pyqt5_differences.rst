Differences Between PyQt6 and PyQt5
===================================

In this section we give an overview of the differences between PyQt6 and PyQt5.
This is not an exhaustive list and does not go into the detail of the
differences between the Qt v6 and Qt v5 APIs.

- All named enums are now implemented as a sub-class of the standard Python
  :py:class:`~enum.Enum` class.  (PyQt5 used :py:class:`~enum.IntEnum` for
  scoped enums and a custom type for traditional named enums).
- Qt provides the :cpp:class:`QFlags` template class as a type-safe way of
  using enum values that can be combined as a set of flags.  The name of the
  class is often the plural form of the name of the enum.  PyQt5 implements
  both of these as separate types.  PyQt6 instead combines them as a single
  type, using the plural name, as a sub-class of :py:class:`~enum.Flag`.
- :py:func:`~PyQt5.QtCore.Q_CLASSINFO` has been replaced by the
  :sip:ref:`~PyQt6.QtCore.pyqtClassInfo` class decorator.
- :py:func:`~PyQt5.QtCore.Q_ENUM`, :py:func:`~PyQt5.QtCore.Q_ENUMS`,
  :py:func:`~PyQt5.QtCore.Q_FLAG` and :py:func:`~PyQt5.QtCore.Q_FLAGS` have
  been replaced by the :sip:ref:`~PyQt6.QtCore.pyqtEnum` class decorator.
- All ``exec_()`` and ``print_()`` methods have been removed.
- :py:attr:`~PyQt5.QtWidgets.qApp` has been removed.
- The :py:const:`~PyQt5.QtCore.PYQT_CONFIGURATION` dict has been removed.
- The :py:mod:`~PyQt5.Qt` module has been removed.
- The bindings for the (GPL licensed) Qt classes that implement support for
  network authorisation have moved out to a separate add-on project
  ``PyQt6-NetworkAuth``.  This means that all of the libraries wrapped by PyQt6
  itself are licensed under the LGPL.
- :program:`pylupdate6` is a completely new pure-Python implementation.  It can
  no longer read a ``.pro`` file in order to determine the names of ``.py``
  files to translate.
- Support for Qt's resource system has been removed (i.e. there is no
  ``pyrcc6``).
- Python v3.6.1 or later is required.

Qt v6 implements a number of functions from Qt v5 that are now marked as being
deprecated.  These are not supported in PyQt6.
