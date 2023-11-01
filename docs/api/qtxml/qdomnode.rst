:orphan:

.. sip:class:: PyQt6.QtXml.QDomNode
    :description: QtXml/QDomNode-c.rst

    .. sip:enum:: PyQt6.QtXml.QDomNode.EncodingPolicy
        :description: QtXml/QDomNode-EncodingPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.EncodingPolicy.EncodingFromDocument
            :description: QtXml/QDomNode-EncodingPolicy-EncodingFromDocument-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.EncodingPolicy.EncodingFromTextStream
            :description: QtXml/QDomNode-EncodingPolicy-EncodingFromTextStream-v.rst

    .. sip:enum:: PyQt6.QtXml.QDomNode.NodeType
        :description: QtXml/QDomNode-NodeType-e.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.AttributeNode
            :description: QtXml/QDomNode-NodeType-AttributeNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.BaseNode
            :description: QtXml/QDomNode-NodeType-BaseNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.CDATASectionNode
            :description: QtXml/QDomNode-NodeType-CDATASectionNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.CharacterDataNode
            :description: QtXml/QDomNode-NodeType-CharacterDataNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.CommentNode
            :description: QtXml/QDomNode-NodeType-CommentNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.DocumentFragmentNode
            :description: QtXml/QDomNode-NodeType-DocumentFragmentNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.DocumentNode
            :description: QtXml/QDomNode-NodeType-DocumentNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.DocumentTypeNode
            :description: QtXml/QDomNode-NodeType-DocumentTypeNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.ElementNode
            :description: QtXml/QDomNode-NodeType-ElementNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.EntityNode
            :description: QtXml/QDomNode-NodeType-EntityNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.EntityReferenceNode
            :description: QtXml/QDomNode-NodeType-EntityReferenceNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.NotationNode
            :description: QtXml/QDomNode-NodeType-NotationNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.ProcessingInstructionNode
            :description: QtXml/QDomNode-NodeType-ProcessingInstructionNode-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomNode.NodeType.TextNode
            :description: QtXml/QDomNode-NodeType-TextNode-v.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.__init__
        :description: QtXml/QDomNode-__init__-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.__init__
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-__init__-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.appendChild
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-appendChild-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.attributes
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap`
        :description: QtXml/QDomNode-attributes-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.childNodes
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNodeList`
        :description: QtXml/QDomNode-childNodes-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.clear
        :description: QtXml/QDomNode-clear-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.cloneNode
        :args:
            deep: bool = True
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-cloneNode-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.columnNumber
        :returns:
            int
        :description: QtXml/QDomNode-columnNumber-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.__eq__
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            bool
        :description: QtXml/QDomNode-__eq__-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.firstChild
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-firstChild-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.firstChildElement
        :args:
            tagName: Optional[str] = ''
            namespaceURI: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomNode-firstChildElement-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.hasAttributes
        :returns:
            bool
        :description: QtXml/QDomNode-hasAttributes-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.hasChildNodes
        :returns:
            bool
        :description: QtXml/QDomNode-hasChildNodes-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.insertAfter
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-insertAfter-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.insertBefore
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-insertBefore-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isAttr
        :returns:
            bool
        :description: QtXml/QDomNode-isAttr-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isCDATASection
        :returns:
            bool
        :description: QtXml/QDomNode-isCDATASection-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isCharacterData
        :returns:
            bool
        :description: QtXml/QDomNode-isCharacterData-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isComment
        :returns:
            bool
        :description: QtXml/QDomNode-isComment-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isDocument
        :returns:
            bool
        :description: QtXml/QDomNode-isDocument-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isDocumentFragment
        :returns:
            bool
        :description: QtXml/QDomNode-isDocumentFragment-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isDocumentType
        :returns:
            bool
        :description: QtXml/QDomNode-isDocumentType-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isElement
        :returns:
            bool
        :description: QtXml/QDomNode-isElement-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isEntity
        :returns:
            bool
        :description: QtXml/QDomNode-isEntity-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isEntityReference
        :returns:
            bool
        :description: QtXml/QDomNode-isEntityReference-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isNotation
        :returns:
            bool
        :description: QtXml/QDomNode-isNotation-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isNull
        :returns:
            bool
        :description: QtXml/QDomNode-isNull-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isProcessingInstruction
        :returns:
            bool
        :description: QtXml/QDomNode-isProcessingInstruction-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isSupported
        :args:
            Optional[str]
            Optional[str]
        :returns:
            bool
        :description: QtXml/QDomNode-isSupported-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.isText
        :returns:
            bool
        :description: QtXml/QDomNode-isText-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.lastChild
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-lastChild-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.lastChildElement
        :args:
            tagName: Optional[str] = ''
            namespaceURI: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomNode-lastChildElement-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.lineNumber
        :returns:
            int
        :description: QtXml/QDomNode-lineNumber-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.localName
        :returns:
            str
        :description: QtXml/QDomNode-localName-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.namedItem
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-namedItem-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.namespaceURI
        :returns:
            str
        :description: QtXml/QDomNode-namespaceURI-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.__ne__
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            bool
        :description: QtXml/QDomNode-__ne__-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.nextSibling
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-nextSibling-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.nextSiblingElement
        :args:
            taName: Optional[str] = ''
            namespaceURI: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomNode-nextSiblingElement-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.nodeName
        :returns:
            str
        :description: QtXml/QDomNode-nodeName-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.nodeType
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType`
        :description: QtXml/QDomNode-nodeType-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.nodeValue
        :returns:
            str
        :description: QtXml/QDomNode-nodeValue-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.normalize
        :description: QtXml/QDomNode-normalize-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.ownerDocument
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomDocument`
        :description: QtXml/QDomNode-ownerDocument-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.parentNode
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-parentNode-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.prefix
        :returns:
            str
        :description: QtXml/QDomNode-prefix-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.previousSibling
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-previousSibling-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.previousSiblingElement
        :args:
            tagName: Optional[str] = ''
            namespaceURI: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomNode-previousSiblingElement-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.removeChild
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-removeChild-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.replaceChild
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomNode-replaceChild-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.save
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
            int
            :sip:ref:`~PyQt6.QtXml.QDomNode.EncodingPolicy`
        :description: QtXml/QDomNode-save-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.setNodeValue
        :args:
            Optional[str]
        :description: QtXml/QDomNode-setNodeValue-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.setPrefix
        :args:
            Optional[str]
        :description: QtXml/QDomNode-setPrefix-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toAttr
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomAttr`
        :description: QtXml/QDomNode-toAttr-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toCDATASection
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomCDATASection`
        :description: QtXml/QDomNode-toCDATASection-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toCharacterData
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomCharacterData`
        :description: QtXml/QDomNode-toCharacterData-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toComment
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomComment`
        :description: QtXml/QDomNode-toComment-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toDocument
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomDocument`
        :description: QtXml/QDomNode-toDocument-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toDocumentFragment
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment`
        :description: QtXml/QDomNode-toDocumentFragment-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toDocumentType
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomDocumentType`
        :description: QtXml/QDomNode-toDocumentType-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toElement
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomNode-toElement-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toEntity
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomEntity`
        :description: QtXml/QDomNode-toEntity-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toEntityReference
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomEntityReference`
        :description: QtXml/QDomNode-toEntityReference-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toNotation
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNotation`
        :description: QtXml/QDomNode-toNotation-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toProcessingInstruction
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction`
        :description: QtXml/QDomNode-toProcessingInstruction-f.rst

    .. sip:method:: PyQt6.QtXml.QDomNode.toText
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomText`
        :description: QtXml/QDomNode-toText-f.rst
