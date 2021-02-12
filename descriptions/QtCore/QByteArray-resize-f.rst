.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: b371b0e4f3d976d2906221526dbac728

Sets the size of the byte array to *size* bytes.

If *size* is greater than the current size, the byte array is extended to make it *size* bytes with the extra bytes added to the end. The new bytes are uninitialized.

If *size* is less than the current size, bytes beyond position *size* are excluded from the byte array.

**Note:** While  will grow the capacity if needed, it never shrinks capacity. To shed excess capacity, use :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.size`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`, :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`.
