.. sip:method-description::
    :status: todo
    :pysig: a100298d86a71a9571987cfec178ed34
    :realsig: (qsizetype,qsizetype) const
    :digest: 22c3472beee3394259048389ce5fc188

Returns a byte array containing *len* bytes from this byte array, starting at position *pos*.

If you know that *pos* and *len* cannot be out of bounds, use :sip:ref:`~PyQt6.QtCore.QByteArray.sliced` instead in new code, because it is faster.

If *len* is -1 (the default), or *pos* + *len* >= :sip:ref:`~PyQt6.QtCore.QByteArray.size`, returns a byte array containing all bytes starting at position *pos* until the end of the byte array.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.last`, :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
