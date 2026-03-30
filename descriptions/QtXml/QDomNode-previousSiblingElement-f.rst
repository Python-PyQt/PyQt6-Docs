.. sip:method-description::
    :status: todo
    :pysig: eacc78dadf18227e6670df784a79f171
    :realsig: (const QString&, const QString&) const
    :digest: ec36d9d210dae5d99d0c3c4c60e373ec

Returns the previous sibling element with tag name *tagName* and namespace URI *namespaceURI*. If *tagName* is empty, returns the previous sibling element with *namespaceURI*, and if *namespaceURI* is empty, returns the previous sibling element with *tagName*. If the both parameters are empty, returns the previous sibling element. Returns a null element if no such sibling exists.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.firstChildElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.nextSiblingElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.lastChildElement`.
