.. sip:method-description::
    :status: todo
    :pysig: cee94c0bc94a0c50a536953bd7eba9e4
    :realsig: (qsizetype, qsizetype, QByteArrayView)
    :digest: 5a86f55a642e7ba31210553216d81edc

Replaces *len* bytes from index position *pos* with the byte array *after*, and returns a reference to this byte array.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 213-216

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.insert`, :sip:ref:`~PyQt6.QtCore.QByteArray.remove`.
