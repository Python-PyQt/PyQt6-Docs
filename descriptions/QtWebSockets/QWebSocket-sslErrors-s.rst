.. sip:signal-description::
    :status: todo
    :pysig: 30abb1de6f61e3fb45b37bea7fd11ba3
    :realsig: (const QList<QSslError>&)
    :digest: 15302ce35260b3333ca177f643d1898e

:sip:ref:`~PyQt6.QtWebSockets.QWebSocket` emits this signal after the SSL handshake to indicate that one or more errors have occurred while establishing the identity of the peer. The errors are usually an indication that :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` is unable to securely identify the peer. Unless any action is taken, the connection will be dropped after this signal has been emitted. If you want to continue connecting despite the errors that have occurred, you must call :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.ignoreSslErrors` from inside a slot connected to this signal. If you need to access the error list at a later point, you can call  (without arguments).

*errors* contains one or more errors that prevent :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` from verifying the identity of the peer.

**Note:** You cannot use :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection` when connecting to this signal, or calling :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.ignoreSslErrors` will have no effect.
