.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: 4c3cf9b3eb1905cd78d72c42b9707ccd

Resizes the bit array to *size* bits.

If *size* is greater than the current size, the bit array is extended to make it *size* bits with the extra bits added to the end. The new bits are initialized to false (0).

If *size* is less than the current size, bits are removed from the end.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBitArray.size`.
