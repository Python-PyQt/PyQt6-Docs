.. sip:method-description::
    :status: todo
    :pysig: c64fe55729abb6664f878077637d7e64
    :realsig: (const QByteArray&)
    :digest: 6dd5fa7a008755fc8ba3bf758152850e

Pings the server to indicate that the connection is still alive. An additional *payload* can be sent along with the ping message.

The size of the *payload* cannot be bigger than 125 bytes. If it is larger, the *payload* is clipped to 125 bytes.

**Note:** :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` and :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` handles ping requests internally, which means they automatically send back a pong response to the peer.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.pong`.
