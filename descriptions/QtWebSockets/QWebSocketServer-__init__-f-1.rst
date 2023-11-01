.. sip:method-description::
    :status: todo
    :pysig: c72f1206380660d0f5263d8da333ae0f
    :realsig: (const QString&, QWebSocketServer::SslMode, QObject*)
    :digest: 34ceef6785100a833e5fddc5cd731fc8

Constructs a new :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` with the given *serverName*. The *serverName* will be used in the HTTP handshake phase to identify the server. It can be empty, in which case no server name will be sent to the client. The *secureMode* parameter indicates whether the server operates over wss (\ :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.SslMode.SecureMode`) or over ws (\ :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.SslMode.NonSecureMode`).

*parent* is passed to the :sip:ref:`~PyQt6.QtCore.QObject` constructor.
