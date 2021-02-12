.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,bool*) const
    :digest: c921cafa6e3902d9cb8d6d5975eeb9ba

Returns the value derived from combining together the values of the *keys* using the OR operator, or -1 if *keys* is not defined. Note that the strings in *keys* must be '|'-separated.

If *keys* is not defined, \*\ *ok* is set to false; otherwise \*\ *ok* is set to true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaEnum.isFlag`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKey`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.valueToKeys`.
