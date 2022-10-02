.. sip:class-description::
    :status: todo
    :brief: Implements a WebSocket-based server
    :digest: fa87b791a7883aada2dd8e020afd57c2

Implements a WebSocket-based server.

It is modeled after :sip:ref:`~PyQt6.QtNetwork.QTcpServer`, and behaves the same. So, if you know how to use :sip:ref:`~PyQt6.QtNetwork.QTcpServer`, you know how to use :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer`. This class makes it possible to accept incoming WebSocket connections. You can specify the port or have :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` pick one automatically. You can listen on a specific address or on all the machine's addresses. Call :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.listen` to have the server listen for incoming connections.

The :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.newConnection` signal is then emitted each time a client connects to the server. Call :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.nextPendingConnection` to accept the pending connection as a connected :sip:ref:`~PyQt6.QtWebSockets.QWebSocket`. The function returns a pointer to a :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` that you can use for communicating with the client.

If an error occurs, :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.serverError` returns the type of error, and :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.errorString` can be called to get a human readable description of what happened.

When listening for connections, the address and port on which the server is listening are available as :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.serverAddress` and :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.serverPort`.

Calling :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.close` makes :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` stop listening for incoming connections.

:sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` currently does not support `WebSocket Extensions <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455#section-9>`_.

**Note:** When working with self-signed certificates, `Firefox bug 594502 <https://doc.qt.io/qt-6/https://bugzilla.mozilla.org/show_bug.cgi?id=594502>`_ prevents `Firefox <https://doc.qt.io/qt-6/https://www.mozilla.org/firefox>`_ to connect to a secure WebSocket server. To work around this problem, first browse to the secure WebSocket server using HTTPS. FireFox will indicate that the certificate is invalid. From here on, the certificate can be added to the exceptions. After this, the secure WebSockets connection should work.

:sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` only supports version 13 of the WebSocket protocol, as outlined in `RFC 6455 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455>`_.

There is a default connection handshake timeout of 10 seconds to avoid denial of service, which can be customized using :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.setHandshakeTimeout`.

.. seealso:: `WebSocket Server Example <https://doc.qt.io/qt-6/echoserver.html>`_, :sip:ref:`~PyQt6.QtWebSockets.QWebSocket`.
