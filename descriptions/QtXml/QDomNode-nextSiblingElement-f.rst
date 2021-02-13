.. sip:method-description::
    :status: todo
    :pysig: 07c332dbd753ea71ba267ff1c8f0138e
    :realsig: (const QString&,const QString&) const
    :digest: ab8112e038df4103a76d4cd53a580fc6

Returns the next sibling element with tag name *tagName* and namespace URI *namespaceURI*. If *tagName* is empty, returns the next sibling element with *namespaceURI*, and if *namespaceURI* is empty, returns the next sibling child element with *tagName*. If the both parameters are empty, returns the next sibling element. Returns a null element if no such sibling exists.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.firstChildElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.previousSiblingElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.lastChildElement`.
