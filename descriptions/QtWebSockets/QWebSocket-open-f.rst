.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 6c6616bcfcb0de30a271e40551ac8601

Opens a WebSocket connection using the given *url*.

If the url contains newline characters (``\r````\n``), then the error signal will be emitted with :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError.ConnectionRefusedError` as error type.
