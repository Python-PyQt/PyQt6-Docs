.. sip:signal-description::
    :status: todo
    :pysig: 9669093f407aca77108e553b30c8d00a
    :realsig: (QSslSocket*,QAbstractSocket::SocketError)
    :digest: 825ce81884b0de120a1ea13e1714a636

This signal is emitted after an error occurred during handshake. The *socketError* parameter describes the type of error that occurred.

The *socket* is automatically deleted after this signal is emitted if the socket handshake has not reached encrypted state. But if the *socket* is successfully encrypted, it is inserted into the :sip:ref:`~PyQt6.QtNetwork.QSslServer`'s pending connections queue. When the user has called :sip:ref:`~PyQt6.QtNetwork.QTcpServer.nextPendingConnection` it is the user's responsibility to destroy the *socket* or the *socket* will not be destroyed until the :sip:ref:`~PyQt6.QtNetwork.QSslServer` object is destroyed. If an error occurs on a *socket* after it has been inserted into the pending connections queue, this signal will not be emitted, and the *socket* will not be removed or destroyed.

**Note:** You cannot use :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection` when connecting to this signal, or the *socket* will have been already destroyed when the signal is handled.

.. seealso:: QSslSocket::error(), errorString().
