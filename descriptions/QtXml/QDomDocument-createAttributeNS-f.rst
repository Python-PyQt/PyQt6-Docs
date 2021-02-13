.. sip:method-description::
    :status: todo
    :pysig: 686e5ed0f1912f3bef5679d8422f6e5f
    :realsig: (const QString&,const QString&)
    :digest: a1c45a63371ed31277f06d54bca58f0d

Creates a new attribute with namespace support that can be inserted into an element. The name of the attribute is *qName* and the namespace URI is *nsURI*. This function also sets :sip:ref:`~PyQt6.QtXml.QDomNode.prefix` and :sip:ref:`~PyQt6.QtXml.QDomNode.localName` to appropriate values (depending on *qName*).

If *qName* is not a valid XML name, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttribute`.
