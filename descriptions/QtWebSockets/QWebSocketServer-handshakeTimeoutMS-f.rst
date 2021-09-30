.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: a1e9d7fd01147cb7fec91f539ea192a7

Returns the handshake timeout for new connections in milliseconds.

The default is 10 seconds. If a peer uses more time to complete the handshake their connection is closed.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.setHandshakeTimeout`, handshakeTimeout().
