.. sip:enum-member-description::
    :status: todo
    :value: 0x04
    :digest: d1e2f51cf06918044fd015e177ad75a7

`RFC 5987 Section 3.2 <https://datatracker.ietf.org/doc/html/rfc5987#section-3.2>`_ required recipients to support ISO-8859-1 ("Latin-1") encoding. When a body-part's file-name contains non-US-ASCII characters that, however, fit into Latin-1, this option prefers to use ISO-8859-1 encoding over UTF-8. The more recent {https://datatracker.ietf.org/doc/html/rfc8187#appendix-A}{RFC 8187} no longer requires ISO-8859-1 support, so the default is to send all non-US-ASCII file-names in UTF-8 encoding instead.
