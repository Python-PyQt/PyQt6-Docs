.. sip:method-description::
    :status: todo
    :pysig: db16aec9ecd33246c705643ec5b17ac2
    :realsig: (const QByteArray&,char)
    :digest: cad88d2fd683929faa2df386dca66571

Decodes *input* from URI/URL-style percent-encoding.

Returns a byte array containing the decoded text. The *percent* parameter allows use of a different character than '%' (for instance, '_' or '=') as the escape character. Equivalent to input.\ :sip:ref:`~PyQt6.QtCore.QByteArray.percentDecoded`\ (percent).

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 494-495

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.percentDecoded`.
