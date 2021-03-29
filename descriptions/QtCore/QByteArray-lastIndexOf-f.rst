.. sip:method-description::
    :status: todo
    :pysig: e4d59d2a16d27f5368f1aec20a3c7147
    :realsig: (QByteArrayView,qsizetype) const
    :digest: c42e7fc4800d90274487726c4004de1e

Returns the index position of the start of the last occurrence of the sequence of bytes viewed by *bv* in this byte array, searching backward from index position *from*. If *from* is -1 (the default), the search starts from the end of the byte array. Returns -1 if no match is found.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 247-252

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.indexOf`, :sip:ref:`~PyQt6.QtCore.QByteArray.contains`, :sip:ref:`~PyQt6.QtCore.QByteArray.count`.
