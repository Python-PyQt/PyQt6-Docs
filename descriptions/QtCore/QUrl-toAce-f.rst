.. sip:method-description::
    :status: todo
    :pysig: b2a1c3086695add31455bfea8040aff8
    :realsig: (const QString&)
    :digest: 4bc4ed6d176e623cd97331464be375e8

Returns the ASCII Compatible Encoding of the given domain name *domain*. The result of this function is considered equivalent to *domain*.

The ASCII-Compatible Encoding (ACE) is defined by RFC 3490, RFC 3491 and RFC 3492. It is part of the Internationalizing Domain Names in Applications (IDNA) specification, which allows for domain names (like ``"example.com"``) to be written using international characters.

This function returns an empty :sip:ref:`~PyQt6.QtCore.QByteArray` if *domain* is not a valid hostname. Note, in particular, that IPv6 literals are not valid domain names.
