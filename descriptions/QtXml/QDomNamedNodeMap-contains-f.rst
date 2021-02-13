.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: 7852dc175504718a5be15f97100c605a

Returns ``true`` if the map contains a node called *name*; otherwise returns ``false``.

**Note:** This function does not take the presence of namespaces into account. Use :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItemNS` to test whether the map contains a node with a specific namespace URI and name.
