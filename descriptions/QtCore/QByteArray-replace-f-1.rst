.. sip:method-description::
    :status: todo
    :pysig: a7d5c9bfe6df32f5020fdfb85d8e258d
    :realsig: (qsizetype,qsizetype,QByteArrayView)
    :digest: 5a86f55a642e7ba31210553216d81edc

Replaces *len* bytes from index position *pos* with the byte array *after*, and returns a reference to this byte array.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 213-216

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.insert`, :sip:ref:`~PyQt6.QtCore.QByteArray.remove`.
