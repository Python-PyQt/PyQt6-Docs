.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 315786e98ab21ac92fc2e30012f2f3aa

Sets the maximum amount of characters a single entity is allowed to expand into to *limit*. If a single entity expands past the given limit, the document is not considered well formed.

The limit is there to prevent DoS attacks when loading unknown XML documents where recursive entity expansion could otherwise exhaust all available memory.

The default value for this property is 4096 characters.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.entityExpansionLimit`.
