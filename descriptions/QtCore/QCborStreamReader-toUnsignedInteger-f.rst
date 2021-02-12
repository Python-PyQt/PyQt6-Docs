.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: ff07176671402dc4ce7dc4d72c92a47c

Returns the unsigned integer value of the current element.

This function does not perform any type conversions, including from boolean or CBOR tag. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isUnsignedInteger` is true; calling it in any other condition is an error.

This function may be used to obtain numbers beyond the range of the return type of :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isUnsignedInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isNegativeInteger`.
