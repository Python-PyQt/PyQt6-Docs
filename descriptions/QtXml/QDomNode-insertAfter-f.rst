.. sip:method-description::
    :status: todo
    :pysig: 7ce1adbc3bce0435338e7d0b8135cc81
    :realsig: (const QDomNode&,const QDomNode&)
    :digest: 3e36501e18a3fd832b44011639b7b180

Inserts the node *newChild* after the child node *refChild*. *refChild* must be a direct child of this node. If *refChild* is :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` then *newChild* is appended as this node's last child.

If *newChild* is the child of another node, it is reparented to this node. If *newChild* is a child of this node, then its position in the list of children is changed.

If *newChild* is a :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment`, then the children of the fragment are removed from the fragment and inserted after *refChild*.

Returns a new reference to *newChild* on success or a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` on failure.

The DOM specification disallow inserting attribute nodes, but due to historical reasons QDom accept them nevertheless.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.replaceChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.removeChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.
