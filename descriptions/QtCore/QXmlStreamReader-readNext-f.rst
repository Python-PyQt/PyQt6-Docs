.. sip:method-description::
    :status: todo
    :pysig: 62e2acfd57fb9018551a212affc1bff1
    :realsig: ()
    :digest: 62dc2ae6b9b56072c4e157360c540bd8

Reads the next token and returns its type.

With one exception, once an :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.error` is reported by , further reading of the XML stream is not possible. Then :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.atEnd` returns ``true``, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.hasError` returns ``true``, and this function returns :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.Invalid`.

The exception is when :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.error` returns :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError`. This error is reported when the end of an otherwise well-formed chunk of XML is reached, but the chunk doesn't represent a complete XML document. In that case, parsing *can* be resumed by calling :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.addData` to add the next chunk of XML, when the stream is being read from a :sip:ref:`~PyQt6.QtCore.QByteArray`, or by waiting for more data to arrive when the stream is being read from a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.device`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.tokenType`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.tokenString`.
