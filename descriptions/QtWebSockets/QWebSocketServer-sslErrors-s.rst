.. sip:signal-description::
    :status: todo
    :pysig: 30abb1de6f61e3fb45b37bea7fd11ba3
    :realsig: (const QList<QSslError>&)
    :digest: f573321f48f707422ecd35e8c7686d65

:sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` emits this signal after the SSL handshake to indicate that one or more errors have occurred while establishing the identity of the peer. The errors are usually an indication that :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` is unable to securely identify the peer. Unless any action is taken, the connection will be dropped after this signal has been emitted.

*errors* contains one or more errors that prevent :sip:ref:`~PyQt6.QtNetwork.QSslSocket` from verifying the identity of the peer.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.peerVerifyError`.
