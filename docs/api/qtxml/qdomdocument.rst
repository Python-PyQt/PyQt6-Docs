:orphan:

.. sip:class:: PyQt6.QtXml.QDomDocument
    :inherits: :sip:ref:`~PyQt6.QtXml.QDomNode`
    :description: QtXml/QDomDocument-c.rst

    .. sip:enum:: PyQt6.QtXml.QDomDocument.ParseOption
        :description: QtXml/QDomDocument-ParseOption-e.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomDocument.ParseOption.Default
            :description: QtXml/QDomDocument-ParseOption-Default-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomDocument.ParseOption.PreserveSpacingOnlyNodes
            :description: QtXml/QDomDocument-ParseOption-PreserveSpacingOnlyNodes-v.rst

        .. sip:enum-member:: PyQt6.QtXml.QDomDocument.ParseOption.UseNamespaceProcessing
            :description: QtXml/QDomDocument-ParseOption-UseNamespaceProcessing-v.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.__init__
        :description: QtXml/QDomDocument-__init__-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.__init__
        :args:
            Optional[str]
        :description: QtXml/QDomDocument-__init__-f-4.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.__init__
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomDocumentType`
        :description: QtXml/QDomDocument-__init__-f-2.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.__init__
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomDocument`
        :description: QtXml/QDomDocument-__init__-f-3.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createAttribute
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomAttr`
        :description: QtXml/QDomDocument-createAttribute-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createAttributeNS
        :args:
            Optional[str]
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomAttr`
        :description: QtXml/QDomDocument-createAttributeNS-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createCDATASection
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomCDATASection`
        :description: QtXml/QDomDocument-createCDATASection-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createComment
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomComment`
        :description: QtXml/QDomDocument-createComment-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createDocumentFragment
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment`
        :description: QtXml/QDomDocument-createDocumentFragment-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createElement
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomDocument-createElement-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createElementNS
        :args:
            Optional[str]
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomDocument-createElementNS-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createEntityReference
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomEntityReference`
        :description: QtXml/QDomDocument-createEntityReference-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createProcessingInstruction
        :args:
            Optional[str]
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction`
        :description: QtXml/QDomDocument-createProcessingInstruction-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.createTextNode
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomText`
        :description: QtXml/QDomDocument-createTextNode-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.doctype
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomDocumentType`
        :description: QtXml/QDomDocument-doctype-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.documentElement
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomDocument-documentElement-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.elementById
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomElement`
        :description: QtXml/QDomDocument-elementById-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.elementsByTagName
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNodeList`
        :description: QtXml/QDomDocument-elementsByTagName-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.elementsByTagNameNS
        :args:
            Optional[str]
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNodeList`
        :description: QtXml/QDomDocument-elementsByTagNameNS-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.implementation
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomImplementation`
        :description: QtXml/QDomDocument-implementation-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.importNode
        :args:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
            bool
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode`
        :description: QtXml/QDomDocument-importNode-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.nodeType
        :returns:
            :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType`
        :description: QtXml/QDomDocument-nodeType-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`
            options: :sip:ref:`~PyQt6.QtXml.QDomDocument.ParseOption` = :sip:ref:`~PyQt6.QtXml.QDomDocument.ParseOption.Default`
        :returns:
            tuple[bool, str, int, int]
        :description: QtXml/QDomDocument-setContent-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            options: :sip:ref:`~PyQt6.QtXml.QDomDocument.ParseOption` = :sip:ref:`~PyQt6.QtXml.QDomDocument.ParseOption.Default`
        :returns:
            tuple[bool, str, int, int]
        :description: QtXml/QDomDocument-setContent-f-1.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            options: :sip:ref:`~PyQt6.QtXml.QDomDocument.ParseOption` = :sip:ref:`~PyQt6.QtXml.QDomDocument.ParseOption.Default`
        :returns:
            tuple[bool, str, int, int]
        :description: QtXml/QDomDocument-setContent-f-2.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            bool
        :returns:
            bool
            str
            int
            int
        :description: QtXml/QDomDocument-setContent-f-11.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            Optional[str]
            bool
        :returns:
            bool
            str
            int
            int
        :description: QtXml/QDomDocument-setContent-f-12.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            bool
        :returns:
            bool
            str
            int
            int
        :description: QtXml/QDomDocument-setContent-f-5.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.setContent
        :args:
            :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`
            bool
        :returns:
            bool
            str
            int
            int
        :description: QtXml/QDomDocument-setContent-f-6.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.toByteArray
        :args:
            indent: int = 1
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtXml/QDomDocument-toByteArray-f.rst

    .. sip:method:: PyQt6.QtXml.QDomDocument.toString
        :args:
            indent: int = 1
        :returns:
            str
        :description: QtXml/QDomDocument-toString-f.rst
