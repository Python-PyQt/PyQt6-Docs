.. sip:method-description::
    :status: todo
    :pysig: d4d85079d3c184e4c59bdc73add11325
    :realsig: (qsizetype,char)
    :digest: f367787d90d7512c9bc048e9ac3e7ee8

Sets the size of the byte array to *newSize* bytes.

If *newSize* is greater than the current size, the byte array is extended to make it *newSize* bytes with the extra bytes added to the end. The new bytes are initialized to *c*.

If *newSize* is less than the current size, bytes beyond position *newSize* are excluded from the byte array.

**Note:** While :sip:ref:`~PyQt6.QtCore.QByteArray.resize` will grow the capacity if needed, it never shrinks capacity. To shed excess capacity, use :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.size`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`, :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`.
