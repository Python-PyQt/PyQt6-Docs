.. sip:method-description::
    :status: todo
    :pysig: 42d9538b9d492682dbfec3b8acd0a489
    :realsig: (const QDomNode&)
    :digest: edbc2c572ee369ea50868809f14853a7

Appends *newChild* as the node's last child.

If *newChild* is the child of another node, it is reparented to this node. If *newChild* is a child of this node, then its position in the list of children is changed.

If *newChild* is a :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment`, then the children of the fragment are removed from the fragment and appended.

If *newChild* is a :sip:ref:`~PyQt6.QtXml.QDomElement` and this node is a :sip:ref:`~PyQt6.QtXml.QDomDocument` that already has an element node as a child, *newChild* is not added as a child and a null node is returned.

Returns a new reference to *newChild* on success or a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` on failure.

Calling this function on a null node(created, for example, with the default constructor) does nothing and returns a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull`.

The DOM specification disallow inserting attribute nodes, but for historical reasons, QDom accepts them anyway.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`, :sip:ref:`~PyQt6.QtXml.QDomNode.replaceChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.removeChild`.
