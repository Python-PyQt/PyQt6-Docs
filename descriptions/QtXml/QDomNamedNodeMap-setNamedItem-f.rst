.. sip:method-description::
    :status: todo
    :pysig: 42d9538b9d492682dbfec3b8acd0a489
    :realsig: (const QDomNode&)
    :digest: 5f128ef289301be9d755237840434561

Inserts the node *newNode* into the named node map. The name used by the map is the node name of *newNode* as returned by :sip:ref:`~PyQt6.QtXml.QDomNode.nodeName`.

If the new node replaces an existing node, i.e. the map contains a node with the same name, the replaced node is returned.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItem`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.removeNamedItem`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItemNS`.
