.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 47a5aaa47b4cff7b334b83c172cd96b4

Sets the identity hint for a preshared key authentication to *hint*. This will affect the next initiated handshake; calling this function on an already-encrypted socket will not affect the socket's identity hint.

The identity hint is used in :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.SslServerMode` only!

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.preSharedKeyIdentityHint`.
