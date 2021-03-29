.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (qsizetype) const
    :digest: 331127efa89a32833e7cce9d9feccd99

Returns a byte array that contains the last *len* bytes of this byte array.

If you know that *len* cannot be out of bounds, use :sip:ref:`~PyQt6.QtCore.QByteArray.last` instead in new code, because it is faster.

The entire byte array is returned if *len* is greater than :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

Returns an empty :sip:ref:`~PyQt6.QtCore.QByteArray` if *len* is smaller than 0.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.endsWith`, :sip:ref:`~PyQt6.QtCore.QByteArray.last`, :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
