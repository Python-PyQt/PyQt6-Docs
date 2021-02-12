.. sip:class-description::
    :status: todo
    :brief: Meta-data about an enumerator
    :digest: 2da4e89103d5bc83da25fbbc5c462bc5

The :sip:ref:`~PyQt6.QtCore.QMetaEnum` class provides meta-data about an enumerator.

Use :sip:ref:`~PyQt6.QtCore.QMetaEnum.name` for the enumerator's name. The enumerator's keys (names of each enumerated item) are returned by :sip:ref:`~PyQt6.QtCore.QMetaEnum.key`; use :sip:ref:`~PyQt6.QtCore.QMetaEnum.keyCount` to find the number of keys. :sip:ref:`~PyQt6.QtCore.QMetaEnum.isFlag` returns whether the enumerator is meant to be used as a flag, meaning that its values can be combined using the OR operator.

The conversion functions :sip:ref:`~PyQt6.QtCore.QMetaEnum.keyToValue`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKey`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.keysToValue`, and :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKeys` allow conversion between the integer representation of an enumeration or set value and its literal representation. The :sip:ref:`~PyQt6.QtCore.QMetaEnum.scope` function returns the class scope this enumerator was declared in.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject`, :sip:ref:`~PyQt6.QtCore.QMetaMethod`, :sip:ref:`~PyQt6.QtCore.QMetaProperty`.
