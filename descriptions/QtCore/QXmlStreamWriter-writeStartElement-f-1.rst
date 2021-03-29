.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&,const QString&)
    :digest: 1e2be072ab44f9d47e6db9659188bb4c

Writes a start element with *name*, prefixed for the specified *namespaceUri*. If the namespace has not been declared yet, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it. Subsequent calls to :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttribute` will add attributes to this element.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeNamespace`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEndElement`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement`.
