.. sip:method-description::
    :status: todo
    :pysig: d93535c5a3d321d03d6ed50f26305666
    :realsig: () const
    :digest: 13770b5bac185ba58f38ec37cb867d03

Returns this connection's current list of elliptic curves. This list is used during the handshake phase for choosing an elliptic curve (when using an elliptic curve cipher). The returned list of curves is ordered by descending preference (i.e., the first curve in the list is the most preferred one).

By default, the handshake phase can choose any of the curves supported by this system's SSL libraries, which may vary from system to system. The list of curves supported by this system's SSL libraries is returned by QSslSocket::supportedEllipticCurves().

You can restrict the list of curves used for choosing the session cipher for this socket by calling :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setEllipticCurves` with a subset of the supported ciphers. You can revert to using the entire set by calling :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setEllipticCurves` with the list returned by QSslSocket::supportedEllipticCurves().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setEllipticCurves`.
