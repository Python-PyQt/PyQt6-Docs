.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 11e4fb72b9075e7268d2546f4bdeec68

Sets the maximum number of certificates in the peer's certificate chain to be checked during the SSL handshake phase, to *depth*. Setting a depth of 0 means that no maximum depth is set, indicating that the whole certificate chain should be checked.

The certificates are checked in issuing order, starting with the peer's own certificate, then its issuer's certificate, and so on.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.peerVerifyDepth`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setPeerVerifyMode`.
