.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: 9789f7bb62d3db8b660e9d8e932a7cd0

Writes an empty element with qualified name *qualifiedName*. Subsequent calls to :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttribute` will add attributes to this element.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
