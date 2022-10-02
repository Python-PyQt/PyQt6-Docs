.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 15674584c67505318f59df1fb84a4e6c

Returns the qualified name of a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.StartElement` or :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.EndElement`;

A qualified name is the raw name of an element in the XML data. It consists of the namespace prefix, followed by colon, followed by the element's local name. Since the namespace prefix is not unique (the same prefix can point to different namespaces and different prefixes can point to the same namespace), you shouldn't use qualifiedName(), but the resolved :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceUri` and the attribute's local :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.name`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.name`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.prefix`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceUri`.
