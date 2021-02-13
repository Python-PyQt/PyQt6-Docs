.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: b41696ee50a1ce6ceeb923c0ac0e91cd

If the node has a namespace prefix, this function changes the namespace prefix of the node to *pre*. Otherwise this function does nothing.

Only nodes of type :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` or :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` can have namespaces. A namespace prefix must have be specified at creation time; it is not possible to add a namespace prefix afterwards.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.prefix`, :sip:ref:`~PyQt6.QtXml.QDomNode.localName`, :sip:ref:`~PyQt6.QtXml.QDomNode.namespaceURI`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS`.
