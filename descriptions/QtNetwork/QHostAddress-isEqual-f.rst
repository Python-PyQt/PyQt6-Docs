.. sip:method-description::
    :status: todo
    :pysig: 86bf6518d2e7fa31a419e952bb0099ba
    :realsig: (const QHostAddress&, QHostAddress::ConversionMode) const
    :digest: db7df007e4d4f005536db6c9a10f28e4

Returns ``true`` if this host address is the same as the *other* address given; otherwise returns ``false``.

The parameter *mode* controls which conversions are performed between addresses of differing protocols. If no *mode* is given, ``TolerantConversion`` is performed by default.

.. seealso:: ConversionMode, operator==().
