.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: c1e65868f40abf81f5b02e4efb0673f5

Returns the maximum number of certificates in the peer's certificate chain to be checked during the SSL handshake phase, or 0 (the default) if no maximum depth has been set, indicating that the whole certificate chain should be checked.

The certificates are checked in issuing order, starting with the peer's own certificate, then its issuer's certificate, and so on.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setPeerVerifyDepth`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerVerifyMode`.
