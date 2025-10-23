.. sip:method-description::
    :status: todo
    :pysig: 6c5df4072896077791688531fc13e62e
    :realsig: (QAnyStringView) const
    :digest: 5de6b0677713d2ec5287c4fe423e625c

Returns the value of the attribute with qualified name *qualifiedName* , or an empty string reference if the attribute is not defined. A qualified name is the raw name of an attribute in the XML data. It consists of the namespace prefix, followed by colon, followed by the attribute's local name. Since the namespace prefix is not unique (the same prefix can point to different namespaces and different prefixes can point to the same namespace), you shouldn't use qualified names, but a resolved namespaceUri and the attribute's local name.

**Note:** In Qt versions prior to 6.6, this function was implemented as an overload set accepting QString and QLatin1StringView only.
