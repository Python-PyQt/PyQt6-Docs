.. sip:method-description::
    :status: todo
    :pysig: e6ae6616716756da8c6dce493448d157
    :realsig: (const QString&, const QString&) const
    :digest: d6929cd49723444390849d1f92d5456c

Returns the node associated with the local name *localName* and the namespace URI *nsURI*.

If the map does not contain such a node, a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItemNS`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItem`.
