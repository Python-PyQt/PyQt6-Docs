.. sip:method-description::
    :status: todo
    :pysig: eacc78dadf18227e6670df784a79f171
    :realsig: (const QString&, const QString&) const
    :digest: 4c30779ced834444e1606afc4a27ded4

Returns the first child element with tag name *tagName* and namespace URI *namespaceURI*. If *tagName* is empty, returns the first child element with *namespaceURI*, and if *namespaceURI* is empty, returns the first child element with *tagName*. If the both parameters are empty, returns the first child element. Returns a null element if no such child exists.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.lastChildElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.previousSiblingElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.nextSiblingElement`.
