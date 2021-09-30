.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 81e07e6ee75f7d8d0a47c90f28ec6d3b

Opens a WebSocket connection using the given *url*.

If the url contains newline characters (\\r\\n), then the error signal will be emitted with :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError.ConnectionRefusedError` as error type.
