.. sip:method-description::
    :status: todo
    :pysig: 377dbe47ca175aea1abba7913de64364
    :realsig: (const QString&)
    :digest: 303a9b13d04ae170719a6256d23cff1d

Returns an :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve` instance representing the named curve *name*. The *name* is the conventional short name for the curve, as represented by RFC 4492 (for instance ``secp521r1``), or as NIST short names (for instance ``P-256``). The actual set of recognized names depends on the SSL implementation.

If the given *name* is not supported, returns an invalid :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve` instance.

**Note:** The OpenSSL implementation of this function treats the name case-sensitively.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve.shortName`.
