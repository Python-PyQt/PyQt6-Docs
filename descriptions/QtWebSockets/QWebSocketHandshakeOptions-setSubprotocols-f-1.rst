.. sip:method-description::
    :status: todo
    :pysig: 2e1e4fde32fc7292dbe8e18ea768734a
    :realsig: (const QStringList&)
    :digest: 0fd69922961a781b79c2d985d7fbd49f

Sets the list of WebSocket subprotocols *protocols* to send along with the websocket handshake.

WebSocket subprotocol names may only consist of those US-ASCII characters that are in the unreserved group. Invalid protocol names will not be included in the handshake.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketHandshakeOptions.subprotocols`.
