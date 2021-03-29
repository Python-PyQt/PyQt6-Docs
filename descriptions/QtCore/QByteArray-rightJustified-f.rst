.. sip:method-description::
    :status: todo
    :pysig: ddc5149a94ed294b5a39ba448d1a7b75
    :realsig: (qsizetype,char,bool) const
    :digest: 8a8615845530b866b27c56975ca8a828

Returns a byte array of size *width* that contains the *fill* byte followed by this byte array.

If *truncate* is false and the size of the byte array is more than *width*, then the returned byte array is a copy of this byte array.

If *truncate* is true and the size of the byte array is more than *width*, then the resulting byte array is truncated at position *width*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 335-336

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.leftJustified`.
