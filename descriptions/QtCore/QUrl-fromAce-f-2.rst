.. sip:method-description::
    :status: todo
    :pysig: 410ea5e3acf4f79ad205082850fbd470
    :realsig: (const QByteArray&, QUrl::AceProcessingOptions)
    :digest: f7ad2293af8850e85a3c1e8c7e05e2b1

Returns the Unicode form of the given domain name *domain*, which is encoded in the ASCII Compatible Encoding (ACE). The output can be customized by passing flags with *options*. The result of this function is considered equivalent to *domain*.

If the value in *domain* cannot be encoded, it will be converted to QString and returned.

The ASCII-Compatible Encoding (ACE) is defined by RFC 3490, RFC 3491 and RFC 3492 and updated by the Unicode Technical Standard #46. It is part of the Internationalizing Domain Names in Applications (IDNA) specification, which allows for domain names (like ``"example.com"``) to be written using non-US-ASCII characters.
