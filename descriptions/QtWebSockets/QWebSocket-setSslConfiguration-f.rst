.. sip:method-description::
    :status: todo
    :pysig: 540d03d543282018ff34d52a022e932e
    :realsig: (const QSslConfiguration&)
    :digest: e74ac1172947a21e4a3f8ea97ad60d79

Sets the socket's SSL configuration to be the contents of *sslConfiguration*.

This function sets the local certificate, the ciphers, the private key and the CA certificates to those stored in *sslConfiguration*. It is not possible to set the SSL-state related fields.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslConfiguration`.
