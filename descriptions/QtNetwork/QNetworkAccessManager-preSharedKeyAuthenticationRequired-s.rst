.. sip:signal-description::
    :status: todo
    :pysig: 135cfff95e2ea0a2f24570d32a364581
    :realsig: (QNetworkReply*,QSslPreSharedKeyAuthenticator*)
    :digest: 9f91d5ab7ae9757bf2ef0c574c0692ac

This signal is emitted if the SSL/TLS handshake negotiates a PSK ciphersuite, and therefore a PSK authentication is then required. The *reply* object is the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` that is negotiating such ciphersuites.

When using PSK, the client must send to the server a valid identity and a valid pre shared key, in order for the SSL handshake to continue. Applications can provide this information in a slot connected to this signal, by filling in the passed *authenticator* object according to their needs.

**Note:** Ignoring this signal, or failing to provide the required credentials, will cause the handshake to fail, and therefore the connection to be aborted.

**Note:** The *authenticator* object is owned by the reply and must not be deleted by the application.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`.
