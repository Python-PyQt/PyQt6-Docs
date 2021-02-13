.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: d5d023cde771d58a1f68eedd4403f04f

Returns the namespace URI of this node or an empty string if the node has no namespace URI.

Only nodes of type :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` or :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` can have namespaces. A namespace URI must be specified at creation time and cannot be changed later.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.prefix`, :sip:ref:`~PyQt6.QtXml.QDomNode.localName`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS`.
