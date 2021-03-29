.. sip:method-description::
    :status: todo
    :pysig: 6818aa644d32f42dbaf0915fde259921
    :realsig: (qsizetype,QByteArrayView)
    :digest: dbcf2b386da63ba7c0aad76676bfa3df

Inserts *data* at index position *i* and returns a reference to this byte array.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 199-201

For large byte arrays, this operation can be slow (`linear time <https://doc.qt.io/qt-6/containers.html#linear-time>`_), because it requires moving all the bytes at indexes *i* and above by at least one position further in memory.

This array grows to accommodate the insertion. If *i* is beyond the end of the array, the array is first extended with space characters to reach this *i*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.append`, :sip:ref:`~PyQt6.QtCore.QByteArray.prepend`, :sip:ref:`~PyQt6.QtCore.QByteArray.replace`, :sip:ref:`~PyQt6.QtCore.QByteArray.remove`.
