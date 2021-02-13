.. sip:method-description::
    :status: todo
    :pysig: 42d9538b9d492682dbfec3b8acd0a489
    :realsig: (const QDomNode&)
    :digest: 2e83cb92ca7fd82bfe95c3b560b92199

Inserts the node *newNode* in the map. If a node with the same namespace URI and the same local name already exists in the map, it is replaced by *newNode*. If the new node replaces an existing node, the replaced node is returned.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItemNS`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.removeNamedItemNS`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItem`.
