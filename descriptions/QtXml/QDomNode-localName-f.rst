.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 0e03dfd6844bdb1f4e8730eda8123b6d

If the node uses namespaces, this function returns the local name of the node; otherwise it returns an empty string.

Only nodes of type :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` or :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` can have namespaces. A namespace must have been specified at creation time; it is not possible to add a namespace afterwards.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.prefix`, :sip:ref:`~PyQt6.QtXml.QDomNode.namespaceURI`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS`.
