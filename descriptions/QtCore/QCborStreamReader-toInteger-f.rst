.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 7a0302083fe1174c56bb60bb40a57d32

Returns the integer value of the current element, be it negative, positive or zero. If the value is larger than 2\ :sup:`63` - 1 or smaller than -2\ :sup:`63`, the returned value will overflow and will have an incorrect sign. If handling those values is required, use :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toUnsignedInteger` or toNegativeInteger() instead.

This function does not perform any type conversions, including from boolean or CBOR tag. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isInteger` is true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toUnsignedInteger`, toNegativeInteger().
