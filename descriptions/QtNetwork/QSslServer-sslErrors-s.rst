.. sip:signal-description::
    :status: todo
    :pysig: d7aee6a60904a60f3f6dbdc6aaf26b29
    :realsig: (QSslSocket*,const QList<QSslError>&)
    :digest: e2eeb6d28d65fb7525ad6c5d276e8d15

:sip:ref:`~PyQt6.QtNetwork.QSslServer` emits this signal after the SSL handshake to indicate that one or more errors have occurred while establishing the identity of the peer. The errors are usually an indication that *socket* is unable to securely identify the peer. Unless any action is taken, the connection will be dropped after this signal has been emitted.

If you want to continue connecting despite the errors that have occurred, you must call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors` from inside a slot connected to this signal. If you need to access the error list at a later point, you can call sslHandshakeErrors().

*errors* contains one or more errors that prevent :sip:ref:`~PyQt6.QtNetwork.QSslSocket` from verifying the identity of the peer.

**Note:** You cannot use :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection` when connecting to this signal, or calling :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors` will have no effect.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslServer.peerVerifyError`.
