.. sip:method-description::
    :status: todo
    :pysig: 4548a82a424de40b70622a91da08ea88
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: c5be2f7128e2848a7cb20b5205349399

This is an overloaded function.

Writes an attribute with *qualifiedName* and *value*.

This function can only be called after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` before any content is written, or after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement`.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
