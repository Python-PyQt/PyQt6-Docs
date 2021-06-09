.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&) const
    :digest: bb072e4fb1fdd578cf1b897cc672b6dd

This is an overloaded function.

Returns the value of the attribute with qualified name *qualifiedName* , or an empty string reference if the attribute is not defined. A qualified name is the raw name of an attribute in the XML data. It consists of the namespace prefix, followed by colon, followed by the attribute's local name. Since the namespace prefix is not unique (the same prefix can point to different namespaces and different prefixes can point to the same namespace), you shouldn't use qualified names, but a resolved namespaceUri and the attribute's local name.
