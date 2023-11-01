.. sip:method-description::
    :status: todo
    :pysig: f6c138623c0183b057ed1bb4983359ca
    :realsig: (QAnyStringView, QAnyStringView, QAnyStringView)
    :digest: 4e6510ac0618eb781839253cc3e5937d

Writes an attribute with *name* and *value*, prefixed for the specified *namespaceUri*. If the namespace has not been declared yet, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it.

This function can only be called after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` before any content is written, or after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement`.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
