.. sip:method-description::
    :status: todo
    :pysig: 32bf9112b9d640ff4b1e217e0aec71df
    :realsig: (const QString&)
    :digest: 0a27e1243ef631b6e6aaedb5ee8abd0f

Returns the element whose ID is equal to *elementId*. If no element with the ID was found, this function returns a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull`.

Since the QDomClasses do not know which attributes are element IDs, this function returns always a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull`. This may change in a future version.
