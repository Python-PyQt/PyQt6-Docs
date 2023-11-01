.. sip:method-description::
    :status: todo
    :pysig: 0746561a4f858394ed78ef5a1502bd3a
    :realsig: (const QString&, const QString&) const
    :digest: 0e26f582dbb316afdc258b173faf522a

Returns the last child element with tag name *tagName* and namespace URI *namespaceURI*. If *tagName* is empty, returns the last child element with *namespaceURI*, and if *namespaceURI* is empty, returns the last child element with *tagName*. If the both parameters are empty, returns the last child element. Returns a null element if no such child exists.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.firstChildElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.previousSiblingElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.nextSiblingElement`.
