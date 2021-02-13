.. sip:method-description::
    :status: todo
    :pysig: dfb0fcf3ad2449423dcdeba19f432fd1
    :realsig: (const QString&) const
    :digest: 12893adc6d78123f0c08472a07d3be1f

Returns the node called *name*.

If the named node map does not contain such a node, a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` is returned. A node's name is the name returned by :sip:ref:`~PyQt6.QtXml.QDomNode.nodeName`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItem`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItemNS`.
