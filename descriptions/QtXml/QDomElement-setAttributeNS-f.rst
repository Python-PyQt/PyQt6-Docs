.. sip:method-description::
    :status: todo
    :pysig: 88ef868705cc2335f9e741fe200ba116
    :realsig: (const QString&,const QString&,const QString&)
    :digest: dc917162f7f5c79aadfaf7300569ccbd

Adds an attribute with the qualified name *qName* and the namespace URI *nsURI* with the value *value*. If an attribute with the same local name and namespace URI exists, its prefix is replaced by the prefix of *qName* and its value is repaced by *value*.

Although *qName* is the qualified name, the local name is used to decide if an existing attribute's value should be replaced.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomElement.attributeNS`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNodeNS`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttribute`.
