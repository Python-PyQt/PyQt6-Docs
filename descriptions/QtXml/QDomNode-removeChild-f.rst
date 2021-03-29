.. sip:method-description::
    :status: todo
    :pysig: 42d9538b9d492682dbfec3b8acd0a489
    :realsig: (const QDomNode&)
    :digest: dfbfd5f9bcbd0659bca2b44a50c5bd78

Removes *oldChild* from the list of children. *oldChild* must be a direct child of this node.

Returns a new reference to *oldChild* on success or a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` on failure.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`, :sip:ref:`~PyQt6.QtXml.QDomNode.replaceChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.
