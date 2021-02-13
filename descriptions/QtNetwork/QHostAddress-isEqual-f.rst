.. sip:method-description::
    :status: todo
    :pysig: 966b50785cb13613814f5a270784870f
    :realsig: (const QHostAddress&,QHostAddress::ConversionMode) const
    :digest: db7df007e4d4f005536db6c9a10f28e4

Returns ``true`` if this host address is the same as the *other* address given; otherwise returns ``false``.

The parameter *mode* controls which conversions are preformed between addresses of differing protocols. If no *mode* is given, ``TolerantConversion`` is performed by default.

.. seealso:: ConversionMode, operator==().
