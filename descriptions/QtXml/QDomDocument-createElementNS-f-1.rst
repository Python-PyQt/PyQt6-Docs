.. sip:method-description::
    :status: todo
    :pysig: 572b474baf9634aa54ee0c656e5566b4
    :realsig: (const QString&, const QString&)
    :digest: 892cda3071de58ebf36811da2bec9997

Creates a new element with namespace support that can be inserted into the DOM tree. The name of the element is *qName* and the namespace URI is *nsURI*. This function also sets :sip:ref:`~PyQt6.QtXml.QDomNode.prefix` and :sip:ref:`~PyQt6.QtXml.QDomNode.localName` to appropriate values (depending on *qName*).

If *qName* is an empty string, returns a null element regardless of whether the invalid data policy is set.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomDocument.createElement`.
