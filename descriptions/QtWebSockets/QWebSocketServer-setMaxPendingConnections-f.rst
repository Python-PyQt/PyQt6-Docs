.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 5b22c3eae3acb592427b877de59f793b

Sets the maximum number of pending accepted connections to *numConnections*. `WebSocketServer <https://doc.qt.io/qt-6/qml-qtwebsockets-websocketserver.html>`_ will accept no more than *numConnections* incoming connections before :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.nextPendingConnection` is called. By default, the limit is 30 pending connections.

:sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` will emit the :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.error` signal with the :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeAbnormalDisconnection` close code when the maximum of connections has been reached. The WebSocket handshake will fail and the socket will be closed.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.maxPendingConnections`, :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.hasPendingConnections`.
