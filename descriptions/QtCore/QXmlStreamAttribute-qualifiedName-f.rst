.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 291ffba9ba2c378605835118963187de

Returns the attribute's qualified name.

A qualified name is the raw name of an attribute in the XML data. It consists of the namespace :sip:ref:`~PyQt6.QtCore.QXmlStreamAttribute.prefix`, followed by colon, followed by the attribute's local :sip:ref:`~PyQt6.QtCore.QXmlStreamAttribute.name`. Since the namespace prefix is not unique (the same prefix can point to different namespaces and different prefixes can point to the same namespace), you shouldn't use , but the resolved :sip:ref:`~PyQt6.QtCore.QXmlStreamAttribute.namespaceUri` and the attribute's local :sip:ref:`~PyQt6.QtCore.QXmlStreamAttribute.name`.
