.. sip:method-description::
    :status: todo
    :pysig: db16aec9ecd33246c705643ec5b17ac2
    :realsig: (const QByteArray&,char)
    :digest: f60886c4fe1c13b166f05307b394d3ea

Returns a decoded copy of the URI/URL-style percent-encoded *input*. The *percent* parameter allows you to replace the '%' character for another (for instance, '_' or '=').

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 494-495

**Note:** Given invalid input (such as a string containing the sequence "%G5", which is not a valid hexadecimal number) the output will be invalid as well. As an example: the sequence "%G5" could be decoded to 'W'.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toPercentEncoding`, :sip:ref:`~PyQt6.QtCore.QUrl.fromPercentEncoding`.
