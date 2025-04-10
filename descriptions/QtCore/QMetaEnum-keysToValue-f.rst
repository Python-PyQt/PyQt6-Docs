.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,bool*) const
    :digest: 43d5217f5dd65419ed4dbeec03057179

Returns the value derived from combining together the values of the *keys* using the OR operator, or -1 if *keys* is not defined. Note that the strings in *keys* must be '|'-separated.

If *keys* is not defined, \*\ *ok* is set to false; otherwise \*\ *ok* is set to true.

If this is a 64-bit enumeration (see :sip:ref:`~PyQt6.QtCore.QMetaEnum.is64Bit`), this function returns the low 32-bit portion of the value. Use keyToValue64() to obtain the full value instead.

.. seealso:: keysToValue64(), :sip:ref:`~PyQt6.QtCore.QMetaEnum.isFlag`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKey`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKeys`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.is64Bit`.
