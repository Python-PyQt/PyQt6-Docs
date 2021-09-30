:orphan:

.. sip:class:: PyQt6.QtCore.QXmlStreamReader
    :description: QtCore/QXmlStreamReader-c.rst

    .. sip:enum:: PyQt6.QtCore.QXmlStreamReader.Error
        :description: QtCore/QXmlStreamReader-Error-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.Error.CustomError
            :description: QtCore/QXmlStreamReader-Error-CustomError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.Error.NoError
            :description: QtCore/QXmlStreamReader-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.Error.NotWellFormedError
            :description: QtCore/QXmlStreamReader-Error-NotWellFormedError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError
            :description: QtCore/QXmlStreamReader-Error-PrematureEndOfDocumentError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.Error.UnexpectedElementError
            :description: QtCore/QXmlStreamReader-Error-UnexpectedElementError-v.rst

    .. sip:enum:: PyQt6.QtCore.QXmlStreamReader.ReadElementTextBehaviour
        :description: QtCore/QXmlStreamReader-ReadElementTextBehaviour-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.ReadElementTextBehaviour.ErrorOnUnexpectedElement
            :description: QtCore/QXmlStreamReader-ReadElementTextBehaviour-ErrorOnUnexpectedElement-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.ReadElementTextBehaviour.IncludeChildElements
            :description: QtCore/QXmlStreamReader-ReadElementTextBehaviour-IncludeChildElements-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.ReadElementTextBehaviour.SkipChildElements
            :description: QtCore/QXmlStreamReader-ReadElementTextBehaviour-SkipChildElements-v.rst

    .. sip:enum:: PyQt6.QtCore.QXmlStreamReader.TokenType
        :description: QtCore/QXmlStreamReader-TokenType-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.Characters
            :description: QtCore/QXmlStreamReader-TokenType-Characters-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.Comment
            :description: QtCore/QXmlStreamReader-TokenType-Comment-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.DTD
            :description: QtCore/QXmlStreamReader-TokenType-DTD-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.EndDocument
            :description: QtCore/QXmlStreamReader-TokenType-EndDocument-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.EndElement
            :description: QtCore/QXmlStreamReader-TokenType-EndElement-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.EntityReference
            :description: QtCore/QXmlStreamReader-TokenType-EntityReference-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.Invalid
            :description: QtCore/QXmlStreamReader-TokenType-Invalid-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.NoToken
            :description: QtCore/QXmlStreamReader-TokenType-NoToken-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.ProcessingInstruction
            :description: QtCore/QXmlStreamReader-TokenType-ProcessingInstruction-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.StartDocument
            :description: QtCore/QXmlStreamReader-TokenType-StartDocument-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QXmlStreamReader.TokenType.StartElement
            :description: QtCore/QXmlStreamReader-TokenType-StartElement-v.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.__init__
        :description: QtCore/QXmlStreamReader-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QXmlStreamReader-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QXmlStreamReader-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.__init__
        :args:
            str
        :description: QtCore/QXmlStreamReader-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.addData
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QXmlStreamReader-addData-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.addData
        :args:
            str
        :description: QtCore/QXmlStreamReader-addData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.addExtraNamespaceDeclaration
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamNamespaceDeclaration`
        :description: QtCore/QXmlStreamReader-addExtraNamespaceDeclaration-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.addExtraNamespaceDeclarations
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QXmlStreamNamespaceDeclaration`]
        :description: QtCore/QXmlStreamReader-addExtraNamespaceDeclarations-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.atEnd
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-atEnd-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.attributes
        :returns:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes`
        :description: QtCore/QXmlStreamReader-attributes-f-1.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.characterOffset
        :returns:
            int
        :description: QtCore/QXmlStreamReader-characterOffset-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.clear
        :description: QtCore/QXmlStreamReader-clear-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.columnNumber
        :returns:
            int
        :description: QtCore/QXmlStreamReader-columnNumber-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QXmlStreamReader-device-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.documentEncoding
        :returns:
            str
        :description: QtCore/QXmlStreamReader-documentEncoding-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.documentVersion
        :returns:
            str
        :description: QtCore/QXmlStreamReader-documentVersion-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.dtdName
        :returns:
            str
        :description: QtCore/QXmlStreamReader-dtdName-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.dtdPublicId
        :returns:
            str
        :description: QtCore/QXmlStreamReader-dtdPublicId-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.dtdSystemId
        :returns:
            str
        :description: QtCore/QXmlStreamReader-dtdSystemId-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.entityDeclarations
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QXmlStreamEntityDeclaration`]
        :description: QtCore/QXmlStreamReader-entityDeclarations-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.entityExpansionLimit
        :returns:
            int
        :description: QtCore/QXmlStreamReader-entityExpansionLimit-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.entityResolver
        :returns:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamEntityResolver`
        :description: QtCore/QXmlStreamReader-entityResolver-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.Error`
        :description: QtCore/QXmlStreamReader-error-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.errorString
        :returns:
            str
        :description: QtCore/QXmlStreamReader-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.hasError
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-hasError-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isCDATA
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isCDATA-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isCharacters
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isCharacters-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isComment
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isComment-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isDTD
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isDTD-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isEndDocument
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isEndDocument-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isEndElement
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isEndElement-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isEntityReference
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isEntityReference-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isProcessingInstruction
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isProcessingInstruction-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isStandaloneDocument
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isStandaloneDocument-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isStartDocument
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isStartDocument-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isStartElement
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isStartElement-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.isWhitespace
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-isWhitespace-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.lineNumber
        :returns:
            int
        :description: QtCore/QXmlStreamReader-lineNumber-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.name
        :returns:
            str
        :description: QtCore/QXmlStreamReader-name-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.namespaceDeclarations
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QXmlStreamNamespaceDeclaration`]
        :description: QtCore/QXmlStreamReader-namespaceDeclarations-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.namespaceProcessing
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-namespaceProcessing-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.namespaceUri
        :returns:
            str
        :description: QtCore/QXmlStreamReader-namespaceUri-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.notationDeclarations
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QXmlStreamNotationDeclaration`]
        :description: QtCore/QXmlStreamReader-notationDeclarations-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.prefix
        :returns:
            str
        :description: QtCore/QXmlStreamReader-prefix-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.processingInstructionData
        :returns:
            str
        :description: QtCore/QXmlStreamReader-processingInstructionData-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.processingInstructionTarget
        :returns:
            str
        :description: QtCore/QXmlStreamReader-processingInstructionTarget-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.qualifiedName
        :returns:
            str
        :description: QtCore/QXmlStreamReader-qualifiedName-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.raiseError
        :args:
            message: str = ''
        :description: QtCore/QXmlStreamReader-raiseError-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.readElementText
        :args:
            behaviour: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.ReadElementTextBehaviour` = :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.ReadElementTextBehaviour.ErrorOnUnexpectedElement`
        :returns:
            str
        :description: QtCore/QXmlStreamReader-readElementText-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.readNext
        :returns:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType`
        :description: QtCore/QXmlStreamReader-readNext-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.readNextStartElement
        :returns:
            bool
        :description: QtCore/QXmlStreamReader-readNextStartElement-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QXmlStreamReader-setDevice-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.setEntityExpansionLimit
        :args:
            int
        :description: QtCore/QXmlStreamReader-setEntityExpansionLimit-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.setEntityResolver
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamEntityResolver`
        :description: QtCore/QXmlStreamReader-setEntityResolver-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.setNamespaceProcessing
        :args:
            bool
        :description: QtCore/QXmlStreamReader-setNamespaceProcessing-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.skipCurrentElement
        :description: QtCore/QXmlStreamReader-skipCurrentElement-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.text
        :returns:
            str
        :description: QtCore/QXmlStreamReader-text-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.tokenString
        :returns:
            str
        :description: QtCore/QXmlStreamReader-tokenString-f.rst

    .. sip:method:: PyQt6.QtCore.QXmlStreamReader.tokenType
        :returns:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType`
        :description: QtCore/QXmlStreamReader-tokenType-f.rst
