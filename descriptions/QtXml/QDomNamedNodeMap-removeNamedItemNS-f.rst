.. sip:method-description::
    :status: todo
    :pysig: 373161a04be39237c52763280d42676e
    :realsig: (const QString&,const QString&)
    :digest: 54466247ef0275c8c4d02317f0ff0557

Removes the node with the local name *localName* and the namespace URI *nsURI* from the map.

The function returns the removed node or a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` if the map did not contain a node with the local name *localName* and the namespace URI *nsURI*.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItemNS`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItemNS`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.removeNamedItem`.
