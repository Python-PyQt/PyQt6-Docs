.. sip:method-description::
    :status: todo
    :pysig: a50799d55bb9bc5bdfdf7194ce5dd41f
    :realsig: () const
    :digest: a3a7dc90bced390039fc88ada63412a7

Returns the peer's chain of digital certificates, starting with the peer's immediate certificate and ending with the CA's certificate.

Peer certificates are checked automatically during the handshake phase. This function is normally used to fetch certificates for display, or for performing connection diagnostics. Certificates contain information about the peer and the certificate issuers, including host name, issuer names, and issuer public keys.

Because the peer certificate is set during the handshake phase, it is safe to access the peer certificate from a slot connected to the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` signal, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors` signal, or the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal.

If an empty list is returned, it can mean the SSL handshake failed, or it can mean the host you are connected to doesn't have a certificate, or it can mean there is no connection.

If you want to get only the peer's immediate certificate, use :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.peerCertificate`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.peerCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors`.
