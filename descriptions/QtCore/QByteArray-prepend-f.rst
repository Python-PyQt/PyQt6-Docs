.. sip:method-description::
    :status: todo
    :pysig: b2cc0c4f8d9f710ef7e89ba9aa900aca
    :realsig: (QByteArrayView)
    :digest: 1330e3efef39d8e1a2883ea80d863ac1

Prepends the byte array view *ba* to this byte array and returns a reference to this byte array.

This operation is typically very fast (`constant time <https://doc.qt.io/qt-6/containers.html#constant-time>`_), because :sip:ref:`~PyQt6.QtCore.QByteArray` preallocates extra space at the beginning of the data, so it can grow without reallocating the entire array each time.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 183-186

This is the same as insert(0, *ba*).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.append`, :sip:ref:`~PyQt6.QtCore.QByteArray.insert`.
