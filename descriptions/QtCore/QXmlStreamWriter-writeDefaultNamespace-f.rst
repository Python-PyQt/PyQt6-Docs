.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 55979a06ba7c8a139b8fd68f33fc7e2e

Writes a default namespace declaration for *namespaceUri*.

If :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` or :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement` was called, the declaration applies to the current element; otherwise it applies to the next child element.

Note that the namespaces *http://www.w3.org/XML/1998/namespace* (bound to *xmlns*) and *http://www.w3.org/2000/xmlns/* (bound to *xml*) by definition cannot be declared as default.
