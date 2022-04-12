.. sip:method-description::
    :status: todo
    :pysig: 1e5d72fbe377c0ce39b787f13159bc23
    :realsig: (const QString&,QUrl::AceProcessingOptions)
    :digest: a673fb77a114c8a99c91f145a931031c

Returns the ASCII Compatible Encoding of the given domain name *domain*. The output can be customized by passing flags with *options*. The result of this function is considered equivalent to *domain*.

The ASCII-Compatible Encoding (ACE) is defined by RFC 3490, RFC 3491 and RFC 3492 and updated by the Unicode Technical Standard #46. It is part of the Internationalizing Domain Names in Applications (IDNA) specification, which allows for domain names (like ``"example.com"``) to be written using non-US-ASCII characters.

This function returns an empty :sip:ref:`~PyQt6.QtCore.QByteArray` if *domain* is not a valid hostname. Note, in particular, that IPv6 literals are not valid domain names.
