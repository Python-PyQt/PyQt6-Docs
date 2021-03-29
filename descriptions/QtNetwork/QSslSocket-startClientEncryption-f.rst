.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d807aefd0a38a33cd3d883995c7aa2a7

Starts a delayed SSL handshake for a client connection. This function can be called when the socket is in the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` but still in the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.UnencryptedMode`. If it is not yet connected, or if it is already encrypted, this function has no effect.

Clients that implement STARTTLS functionality often make use of delayed SSL handshakes. Most other clients can avoid calling this function directly by using :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted` instead, which automatically performs the handshake.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.startServerEncryption`.
