.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: 5af0321bd5171013db33fda829d5459d

Writes a default namespace declaration for *namespaceUri*.

If :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` or :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement` was called, the declaration applies to the current element; otherwise it applies to the next child element.

Note that the namespaces *http://www.w3.org/XML/1998/namespace* (bound to *xmlns*) and *http://www.w3.org/2000/xmlns/* (bound to *xml*) by definition cannot be declared as default.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
