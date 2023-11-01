.. sip:method-description::
    :status: todo
    :pysig: 31c2d3982cfaf905cac8e2c6560b0db1
    :realsig: (const QString&, const QString&, const QString&)
    :digest: dc917162f7f5c79aadfaf7300569ccbd

Adds an attribute with the qualified name *qName* and the namespace URI *nsURI* with the value *value*. If an attribute with the same local name and namespace URI exists, its prefix is replaced by the prefix of *qName* and its value is replaced by *value*.

Although *qName* is the qualified name, the local name is used to decide if an existing attribute's value should be replaced.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomElement.attributeNS`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNodeNS`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttribute`.
