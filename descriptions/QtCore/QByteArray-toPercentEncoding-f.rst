.. sip:method-description::
    :status: todo
    :pysig: 60d722787cf57d1d168d0ebc15c6bbd0
    :realsig: (const QByteArray&,const QByteArray&,char) const
    :digest: b85df4d1ebda6b3d23c2efe878008e08

Returns a URI/URL-style percent-encoded copy of this byte array. The *percent* parameter allows you to override the default '%' character for another.

By default, this function will encode all bytes that are not one of the following:

ALPHA ("a" to "z" and "A" to "Z") / DIGIT (0 to 9) / "-" / "." / "_" / "~"

To prevent bytes from being encoded pass them to *exclude*. To force bytes to be encoded pass them to *include*. The *percent* character is always encoded.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 499-502

The hex encoding uses the numbers 0-9 and the uppercase letters A-F.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.fromPercentEncoding`, :sip:ref:`~PyQt6.QtCore.QUrl.toPercentEncoding`.
