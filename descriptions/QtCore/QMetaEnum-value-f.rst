.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: dafb4f295955014fba6cd617c1acaa56

Returns the value with the given *index*; or returns -1 if there is no such value.

If this is an enumeration with a 64-bit underlying type (see :sip:ref:`~PyQt6.QtCore.QMetaEnum.is64Bit`), this function returns the low 32-bit portion of the value. Use value64() to obtain the full value instead.

.. seealso:: value64(), :sip:ref:`~PyQt6.QtCore.QMetaEnum.keyCount`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.key`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.keyToValue`.
