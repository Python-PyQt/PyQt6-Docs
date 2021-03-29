.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 469e4609ab2778c2fdbba8af3c274c59

Returns the namespace prefix of the node or an empty string if the node has no namespace prefix.

Only nodes of type :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` or :sip:ref:`~PyQt6.QtXml.QDomNode.NodeType` can have namespaces. A namespace prefix must be specified at creation time. If a node was created with a namespace prefix, you can change it later with :sip:ref:`~PyQt6.QtXml.QDomNode.setPrefix`.

If you create an element or attribute with :sip:ref:`~PyQt6.QtXml.QDomDocument.createElement` or :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttribute`, the prefix will be an empty string. If you use :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS` or :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS` instead, the prefix will not be an empty string; but it might be an empty string if the name does not have a prefix.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.setPrefix`, :sip:ref:`~PyQt6.QtXml.QDomNode.localName`, :sip:ref:`~PyQt6.QtXml.QDomNode.namespaceURI`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS`.
