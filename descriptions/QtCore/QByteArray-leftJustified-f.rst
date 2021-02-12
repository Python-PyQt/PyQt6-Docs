.. sip:method-description::
    :status: todo
    :pysig: ddc5149a94ed294b5a39ba448d1a7b75
    :realsig: (qsizetype,char,bool) const
    :digest: 554bb676be1410d8d8bac7140a7af898

Returns a byte array of size *width* that contains this byte array padded with the *fill* byte.

If *truncate* is false and the :sip:ref:`~PyQt6.QtCore.QByteArray.size` of the byte array is more than *width*, then the returned byte array is a copy of this byte array.

If *truncate* is true and the :sip:ref:`~PyQt6.QtCore.QByteArray.size` of the byte array is more than *width*, then any bytes in a copy of the byte array after position *width* are removed, and the copy is returned.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 329-330

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.rightJustified`.
