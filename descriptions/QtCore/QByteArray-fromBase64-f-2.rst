.. sip:method-description::
    :status: todo
    :pysig: b2c9e3b30bee0f5a27feb6f705a716dd
    :realsig: (const QByteArray&, QByteArray::Base64Options)
    :digest: 8a7d2e50899f13eecf46bcf67c3d6238

Returns a decoded copy of the Base64 array *base64*, using the options defined by *options*. If *options* contains ``IgnoreBase64DecodingErrors`` (the default), the input is not checked for validity; invalid characters in the input are skipped, enabling the decoding process to continue with subsequent characters. If *options* contains ``AbortOnBase64DecodingErrors``, then decoding will stop at the first invalid character.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 422-426

The algorithm used to decode Base64-encoded data is defined in RFC 4648.

Returns the decoded data, or, if the ``AbortOnBase64DecodingErrors`` option was passed and the input data was invalid, an empty byte array.

**Note:** The :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64Encoding` function is recommended in new code.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toBase64`, :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64Encoding`.
