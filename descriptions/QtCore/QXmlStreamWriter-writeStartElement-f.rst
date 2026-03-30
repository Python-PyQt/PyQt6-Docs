.. sip:method-description::
    :status: todo
    :pysig: 48964e5682cadc964cb6cdcfffc910dc
    :realsig: (QAnyStringView)
    :digest: ca19c8160bb37bd3a0c1de64bb369b08

Writes a start element with *qualifiedName*. Subsequent calls to :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttribute` will add attributes to this element.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEndElement`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement`.
