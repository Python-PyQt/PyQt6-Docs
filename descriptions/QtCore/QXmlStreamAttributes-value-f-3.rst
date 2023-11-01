.. sip:method-description::
    :status: todo
    :pysig: a8016cef068f98551d1cad0d7bc18b61
    :realsig: (QAnyStringView, QAnyStringView) const
    :digest: 01f7732f29f50c1aad1bd1658bd6aec0

Returns the value of the attribute *name* in the namespace described with *namespaceUri*, or an empty string reference if the attribute is not defined. The *namespaceUri* can be empty.

**Note:** In Qt versions prior to 6.6, this function was implemented as an overload set accepting combinations of QString and QLatin1StringView only.
