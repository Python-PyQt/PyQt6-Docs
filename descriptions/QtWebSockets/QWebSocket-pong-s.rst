.. sip:signal-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (quint64,const QByteArray&)
    :digest: 08428455a487596dac90d1dc373fa903

Emitted when a pong message is received in reply to a previous ping. *elapsedTime* contains the roundtrip time in milliseconds and *payload* contains an optional payload that was sent with the ping.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.ping`.
