.. sip:method-description::
    :status: todo
    :pysig: 5b5f0037effa64dcfdc4b07c83e631b9
    :realsig: () const
    :digest: 652826980a3bcdf0fe5e73dc7e30a5cf

Returns value of the current simple type.

This function does not perform any type conversions, including from integer. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType` is true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isTrue`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFalse`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isBool`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isNull`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isUndefined`.
