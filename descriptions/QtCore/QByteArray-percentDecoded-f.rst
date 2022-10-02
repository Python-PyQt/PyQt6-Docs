.. sip:method-description::
    :status: todo
    :pysig: 2ef13145860868eaca29725a22e4fbe5
    :realsig: (char) const
    :digest: 4200811405445b72d2ffe798acb1d06f

Decodes URI/URL-style percent-encoding.

Returns a byte array containing the decoded text. The *percent* parameter allows use of a different character than '%' (for instance, '_' or '=') as the escape character.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py

**Note:** Given invalid input (such as a string containing the sequence "%G5", which is not a valid hexadecimal number) the output will be invalid as well. As an example: the sequence "%G5" could be decoded to 'W'.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toPercentEncoding`, :sip:ref:`~PyQt6.QtCore.QUrl.fromPercentEncoding`.
