.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&,const QString&)
    :digest: d11994c8f18f6baf08a5a59098287510

Writes an empty element with *name*, prefixed for the specified *namespaceUri*. If the namespace has not been declared, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it. Subsequent calls to :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttribute` will add attributes to this element.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeNamespace`.
