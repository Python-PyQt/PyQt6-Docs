.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: 5cdd7f00c945b56024b533bdea6f79e8

Returns ``true`` if this :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes` has an attribute whose qualified name is *qualifiedName*; otherwise returns ``false``.

Note that this is not namespace aware. For instance, if this :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes` contains an attribute whose lexical name is "xlink:href" this doesn't tell that an attribute named ``href`` in the XLink namespace is present, since the ``xlink`` prefix can be bound to any namespace. Use the overload that takes a namespace URI and a local name as parameter, for namespace aware code.
