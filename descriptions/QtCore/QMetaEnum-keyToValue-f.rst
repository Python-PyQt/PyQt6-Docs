.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,bool*) const
    :digest: 272a497ceb38e045be83ab1adcc5b236

Returns the integer value of the given enumeration *key*, or -1 if *key* is not defined.

If *key* is not defined, \*\ *ok* is set to false; otherwise \*\ *ok* is set to true.

For flag types, use :sip:ref:`~PyQt6.QtCore.QMetaEnum.keysToValue`.

If this is a 64-bit enumeration (see :sip:ref:`~PyQt6.QtCore.QMetaEnum.is64Bit`), this function returns the low 32-bit portion of the value. Use keyToValue64() to obtain the full value instead.

.. seealso:: keyToValue64, :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKey`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.isFlag`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.keysToValue`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.is64Bit`.
