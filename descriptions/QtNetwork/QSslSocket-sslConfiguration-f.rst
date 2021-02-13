.. sip:method-description::
    :status: todo
    :pysig: 540d03d543282018ff34d52a022e932e
    :realsig: () const
    :digest: e7b31dd1740a0894b05107d24df6fefe

Returns the socket's SSL configuration state. The default SSL configuration of a socket is to use the default ciphers, default CA certificates, no local private key or certificate.

The SSL configuration also contains fields that can change with time without notice.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setSslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.localCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerCertificateChain`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sessionCipher`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.privateKey`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ciphers`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.caCertificates`.
