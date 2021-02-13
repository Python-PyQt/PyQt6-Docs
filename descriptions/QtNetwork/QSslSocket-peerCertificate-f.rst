.. sip:method-description::
    :status: todo
    :pysig: b3c432d61e79f3a1841b7e0cdc24270d
    :realsig: () const
    :digest: 49dc18bf5021c46b348514c129b79ff9

Returns the peer's digital certificate (i.e., the immediate certificate of the host you are connected to), or a null certificate, if the peer has not assigned a certificate.

The peer certificate is checked automatically during the handshake phase, so this function is normally used to fetch the certificate for display or for connection diagnostic purposes. It contains information about the peer, including its host name, the certificate issuer, and the peer's public key.

Because the peer certificate is set during the handshake phase, it is safe to access the peer certificate from a slot connected to the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` signal or the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal.

If a null certificate is returned, it can mean the SSL handshake failed, or it can mean the host you are connected to doesn't have a certificate, or it can mean there is no connection.

If you want to check the peer's complete chain of certificates, use :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerCertificateChain` to get them all at once.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerCertificateChain`.
