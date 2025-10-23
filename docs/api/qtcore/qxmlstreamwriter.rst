:orphan:

.. sip:class:: PyQt6.QtCore.QXmlStreamWriter
    :description: QtCore/QXmlStreamWriter-c.rst

    .. sip:enum:: PyQt6.QtCore.QXmlStreamWriter.Error
        :description: QtCore/QXmlStreamWriter-Error-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamWriter.Error.Custom
            :description: QtCore/QXmlStreamWriter-Error-Custom-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamWriter.Error.Encoding
            :description: QtCore/QXmlStreamWriter-Error-Encoding-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamWriter.Error.InvalidCharacter
            :description: QtCore/QXmlStreamWriter-Error-InvalidCharacter-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamWriter.Error.IO
            :description: QtCore/QXmlStreamWriter-Error-IO-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamWriter.Error.None_
            :description: QtCore/QXmlStreamWriter-Error-None_-v.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.__init__
        :description: QtCore/QXmlStreamWriter-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QXmlStreamWriter-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QXmlStreamWriter-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.autoFormatting
        :returns:
            bool
        :description: QtCore/QXmlStreamWriter-autoFormatting-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.autoFormattingIndent
        :returns:
            int
        :description: QtCore/QXmlStreamWriter-autoFormattingIndent-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QXmlStreamWriter-device-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.Error`
        :description: QtCore/QXmlStreamWriter-error-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.errorString
        :returns:
            str
        :description: QtCore/QXmlStreamWriter-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.hasError
        :returns:
            bool
        :description: QtCore/QXmlStreamWriter-hasError-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.raiseError
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-raiseError-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.setAutoFormatting
        :args:
            bool
        :description: QtCore/QXmlStreamWriter-setAutoFormatting-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.setAutoFormattingIndent
        :args:
            int
        :description: QtCore/QXmlStreamWriter-setAutoFormattingIndent-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QXmlStreamWriter-setDevice-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.setStopWritingOnError
        :args:
            bool
        :description: QtCore/QXmlStreamWriter-setStopWritingOnError-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.stopWritingOnError
        :returns:
            bool
        :description: QtCore/QXmlStreamWriter-stopWritingOnError-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeAttribute
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamAttribute`
        :description: QtCore/QXmlStreamWriter-writeAttribute-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeAttribute
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeAttribute-f-5.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeAttribute
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeAttribute-f-6.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeAttributes
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes`
        :description: QtCore/QXmlStreamWriter-writeAttributes-f-1.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeCDATA
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeCDATA-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeCharacters
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeCharacters-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeComment
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeComment-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeCurrentToken
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`
        :description: QtCore/QXmlStreamWriter-writeCurrentToken-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeDefaultNamespace
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeDefaultNamespace-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeDTD
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeDTD-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeEmptyElement-f-4.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeEmptyElement-f-5.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeEndDocument
        :description: QtCore/QXmlStreamWriter-writeEndDocument-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeEndElement
        :description: QtCore/QXmlStreamWriter-writeEndElement-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeEntityReference
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeEntityReference-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeNamespace
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            prefix: Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]] = ''
        :description: QtCore/QXmlStreamWriter-writeNamespace-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeProcessingInstruction
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            data: Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]] = ''
        :description: QtCore/QXmlStreamWriter-writeProcessingInstruction-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeStartDocument
        :description: QtCore/QXmlStreamWriter-writeStartDocument-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeStartDocument
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeStartDocument-f-5.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeStartDocument
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            bool
        :description: QtCore/QXmlStreamWriter-writeStartDocument-f-6.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeStartElement
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeStartElement-f-4.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeStartElement
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeStartElement-f-5.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeTextElement
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeTextElement-f-4.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamWriter.writeTextElement
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QXmlStreamWriter-writeTextElement-f-5.rst
