.. sip:method-description::
    :status: todo
    :pysig: 1e00aa8c3f12a0e571ee4dd99254973b
    :realsig: (const QByteArray&)
    :digest: 0aa351ec601c6ede562ff1410eedd566

Pings the server to indicate that the connection is still alive. Additional *payload* can be sent along the ping message.

The size of the *payload* cannot be bigger than 125. If it is larger, the *payload* is clipped to 125 bytes.

**Note:** :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` and :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` handles ping requests internally, which means they automatically send back a pong response to the peer.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.pong`.
