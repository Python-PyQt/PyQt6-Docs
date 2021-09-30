.. sip:signal-description::
    :status: todo
    :pysig: 0ba96fff41a53a4f51e7c6334ff043b0
    :realsig: (QSslPreSharedKeyAuthenticator*)
    :digest: 114c935a1b6e286911b8c6350452b6f4

:sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` emits this signal when it negotiates a PSK ciphersuite, and therefore a PSK authentication is then required.

When using PSK, the client must send to the server a valid identity and a valid pre shared key, in order for the SSL handshake to continue. Applications can provide this information in a slot connected to this signal, by filling in the passed *authenticator* object according to their needs.

**Note:** Ignoring this signal, or failing to provide the required credentials, will cause the handshake to fail, and therefore the connection to be aborted.

**Note:** The *authenticator* object is owned by the socket and must not be deleted by the application.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.preSharedKeyAuthenticationRequired`.
