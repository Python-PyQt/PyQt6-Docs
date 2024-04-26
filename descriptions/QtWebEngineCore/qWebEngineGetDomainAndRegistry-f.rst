.. sip:method-description::
    :status: todo
    :pysig: c23ad6917e655090d33036c53c10d649
    :realsig: (const QUrl&)
    :digest: 8a2a4c9fb182aed5d07319b2c55d145c

Returns the domain of the host, that is, the effective top-level domain (eTLD) and the first domain below it, from *url*.

This function supports internationalized domain names (IDN). In this case, it returns the domain encoded in Punycode.

If the host is not a domain, returns an empty string.
