.. sip:method-description::
    :status: todo
    :pysig: 88ef868705cc2335f9e741fe200ba116
    :realsig: (const QString&,const QString&,const QString&)
    :digest: 2da29230cf0ef3229c3a81f9a508e85f

Writes an attribute with *name* and *value*, prefixed for the specified *namespaceUri*. If the namespace has not been declared yet, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it.

This function can only be called after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` before any content is written, or after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement`.
