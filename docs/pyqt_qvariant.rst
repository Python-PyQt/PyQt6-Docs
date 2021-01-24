.. _ref-qvariant:

Support for :sip:ref:`~PyQt6.QtCore.QVariant`
=============================================

PyQt6 can convert any Python object to a :sip:ref:`~PyQt6.QtCore.QVariant` and
back again.  Normally this is done automatically and transparently so you don't
even need to know of the existence of :sip:ref:`~PyQt6.QtCore.QVariant`.

An invalid :sip:ref:`~PyQt6.QtCore.QVariant` is automatically converted to
``None`` and vice versa.

However there are some situations where you might need to exert more control.
For example you might want to distinguish between a
:sip:ref:`~PyQt6.QtCore.QVariant` containing a C++ float value and one
containing a C++ double value.

However it is possible to temporarily suppress the automatic conversion of a
C++ :sip:ref:`~PyQt6.QtCore.QVariant` to a Python object and to return a
wrapped Python :sip:ref:`~PyQt6.QtCore.QVariant` instead
by calling the :py:func:`~PyQt6.sip.enableautoconversion` function.

The actual value of a wrapped Python :sip:ref:`~PyQt6.QtCore.QVariant` is
obtained by calling its :sip:ref:`~PyQt6.QtCore.QVariant.value` method.
