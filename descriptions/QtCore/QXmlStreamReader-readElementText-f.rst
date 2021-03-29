.. sip:method-description::
    :status: todo
    :pysig: fef1ef5a6b432c5f2ad873d0c7282b5e
    :realsig: (QXmlStreamReader::ReadElementTextBehaviour)
    :digest: b4f6caabbb147ff55454eb0d69f5dd6a

Convenience function to be called in case a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.StartElement` was read. Reads until the corresponding :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.EndElement` and returns all text in-between. In case of no error, the current token (see :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.tokenType`) after having called this function is :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.EndElement`.

The function concatenates :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.text` when it reads either :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.Characters` or :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.EntityReference` tokens, but skips :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.ProcessingInstruction` and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.Comment`. If the current token is not :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.StartElement`, an empty string is returned.

The *behaviour* defines what happens in case anything else is read before reaching :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.EndElement`. The function can include the text from child elements (useful for example for HTML), ignore child elements, or raise an :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.Error.UnexpectedElementError` and return what was read so far (default).
