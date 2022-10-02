.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 0fd69922961a781b79c2d985d7fbd49f

Sets the list of WebSocket subprotocols *protocols* to send along with the websocket handshake.

WebSocket subprotocol names may only consist of those US-ASCII characters that are in the unreserved group. Invalid protocol names will not be included in the handshake.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketHandshakeOptions.subprotocols`.
