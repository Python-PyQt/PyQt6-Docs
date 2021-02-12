.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,bool*) const
    :digest: 42fccb0ad52cd591d450f0d281337442

Returns the integer value of the given enumeration *key*, or -1 if *key* is not defined.

If *key* is not defined, \*\ *ok* is set to false; otherwise \*\ *ok* is set to true.

For flag types, use :sip:ref:`~PyQt6.QtCore.QMetaEnum.keysToValue`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKey`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.isFlag`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.keysToValue`.
