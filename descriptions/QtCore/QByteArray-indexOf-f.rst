.. sip:method-description::
    :status: todo
    :pysig: 155689fb3ea0161afa7a8b8a4e0992c8
    :realsig: (QByteArrayView,qsizetype) const
    :digest: 4b9e61d3bdeabd4ede8c785af3651fa5

Returns the index position of the start of the first occurrence of the sequence of bytes viewed by *bv* in this byte array, searching forward from index position *from*. Returns -1 if no match is found.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 228-233

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.lastIndexOf`, :sip:ref:`~PyQt6.QtCore.QByteArray.contains`, :sip:ref:`~PyQt6.QtCore.QByteArray.count`.
