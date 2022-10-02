.. sip:method-description::
    :status: todo
    :pysig: 5c46948606a7b8b63fc5cdfad1789a50
    :realsig: (const QByteArray&,bool,QString*,int*,int*)
    :digest: 132d31d9a276e3d6ab0d942ddc1f39d7

This function parses the XML document from the byte array *data* and sets it as the content of the document. It tries to detect the encoding of the document as required by the XML specification.

If *namespaceProcessing* is true, the parser recognizes namespaces in the XML file and sets the prefix name, local name and namespace URI to appropriate values. If *namespaceProcessing* is false, the parser does no namespace processing when it reads the XML file.

If a parse error occurs, this function returns ``false`` and the error message is placed in ``\*``\ *errorMsg*, the line number in ``\*``\ *errorLine* and the column number in ``\*``\ *errorColumn* (unless the associated pointer is set to ``nullptr``); otherwise this function returns ``true``.

If *namespaceProcessing* is true, the function :sip:ref:`~PyQt6.QtXml.QDomNode.prefix` returns a string for all elements and attributes. It returns an empty string if the element or attribute has no prefix.

Text nodes consisting only of whitespace are stripped and won't appear in the :sip:ref:`~PyQt6.QtXml.QDomDocument`.

If *namespaceProcessing* is false, the functions :sip:ref:`~PyQt6.QtXml.QDomNode.prefix`, :sip:ref:`~PyQt6.QtXml.QDomNode.localName` and :sip:ref:`~PyQt6.QtXml.QDomNode.namespaceURI` return an empty string.

Entity references are handled as follows:

* References to internal general entities and character entities occurring in the content are included. The result is a :sip:ref:`~PyQt6.QtXml.QDomText` node with the references replaced by their corresponding entity values.

* References to parameter entities occurring in the internal subset are included. The result is a :sip:ref:`~PyQt6.QtXml.QDomDocumentType` node which contains entity and notation declarations with the references replaced by their corresponding entity values.

* Any general parsed entity reference which is not defined in the internal subset and which occurs in the content is represented as a :sip:ref:`~PyQt6.QtXml.QDomEntityReference` node.

* Any parsed entity reference which is not defined in the internal subset and which occurs outside of the content is replaced with an empty string.

* Any unparsed entity reference is replaced with an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.namespaceURI`, :sip:ref:`~PyQt6.QtXml.QDomNode.localName`, :sip:ref:`~PyQt6.QtXml.QDomNode.prefix`, QString::isNull(), QString::isEmpty().
