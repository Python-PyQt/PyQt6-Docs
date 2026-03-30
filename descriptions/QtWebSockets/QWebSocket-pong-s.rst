.. sip:signal-description::
    :status: todo
    :pysig: 7235a47c1a42414dac96dde9c65d8778
    :realsig: (quint64, const QByteArray&)
    :digest: 08428455a487596dac90d1dc373fa903

Emitted when a pong message is received in reply to a previous ping. *elapsedTime* contains the roundtrip time in milliseconds and *payload* contains an optional payload that was sent with the ping.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.ping`.
