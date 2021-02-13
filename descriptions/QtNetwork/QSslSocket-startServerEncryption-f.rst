.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b60662064c8a62d6f94a4e4520c486c5

Starts a delayed SSL handshake for a server connection. This function can be called when the socket is in the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` but still in :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.UnencryptedMode`. If it is not connected or it is already encrypted, the function has no effect.

For server sockets, calling this function is the only way to initiate the SSL handshake. Most servers will call this function immediately upon receiving a connection, or as a result of having received a protocol-specific command to enter SSL mode (e.g, the server may respond to receiving the string "STARTTLS\\r\\n" by calling this function).

The most common way to implement an SSL server is to create a subclass of :sip:ref:`~PyQt6.QtNetwork.QTcpServer` and reimplement :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection`. The returned socket descriptor is then passed to :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setSocketDescriptor`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.startClientEncryption`.
