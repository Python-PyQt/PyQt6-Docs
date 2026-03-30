.. sip:method-description::
    :status: todo
    :pysig: 4069b4ec285be3d21ff07d16fa7e95a7
    :realsig: (const QHostAddress&, quint16)
    :digest: 7dd3a4bda8aa40476db9fb4689db97b6

Tells the server to listen for incoming connections on address *address* and port *port*. If *port* is 0, a port is chosen automatically. If *address* is :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any`, the server will listen on all network interfaces.

Returns true on success; otherwise returns false.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.isListening`.
