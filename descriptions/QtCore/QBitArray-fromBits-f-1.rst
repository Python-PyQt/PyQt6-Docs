.. sip:method-description::
    :status: todo
    :pysig: fe9bc9c8821ffee9aa219b51fd49e0fa
    :realsig: (const char*,qsizetype)
    :digest: 68f4e1d3481389ffc4398a2097f85211

Creates a :sip:ref:`~PyQt6.QtCore.QBitArray` with the dense bit array located at *data*, with *size* bits. The byte array at *data* must be at least *size* / 8 (rounded up) bytes long.

If *size* is not a multiple of 8, this function will include the lowest *size* % 8 bits from the last byte in *data*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBitArray.bits`.
