.. sip:method-description::
    :status: todo
    :pysig: f45a17c6dcf6e98f9500503a415c43aa
    :realsig: (const QUrl&,const QWebSocketHandshakeOptions&)
    :digest: b2650dbd28060969170c5808ded0e4eb

Opens a WebSocket connection using the given *url* and *options*.

If the url contains newline characters (\\r\\n), then the error signal will be emitted with :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError.ConnectionRefusedError` as error type.

Additional options for the WebSocket handshake such as subprotocols can be specified in *options*.
