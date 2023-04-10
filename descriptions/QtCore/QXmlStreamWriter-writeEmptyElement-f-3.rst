.. sip:method-description::
    :status: todo
    :pysig: 629c6966eefeb1bb758f4f8a9417e613
    :realsig: (QAnyStringView,QAnyStringView)
    :digest: 2d1981fabcbef979e90861e693dfb09a

Writes an empty element with *name*, prefixed for the specified *namespaceUri*. If the namespace has not been declared, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it. Subsequent calls to :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttribute` will add attributes to this element.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeNamespace`.
