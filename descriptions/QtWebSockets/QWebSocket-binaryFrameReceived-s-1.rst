.. sip:signal-description::
    :status: todo
    :pysig: 818ceb9f7882cf71214966cf00526abf
    :realsig: (const QByteArray&, bool)
    :digest: b2194267fb67d8a35069d28b12fc8d9f

This signal is emitted whenever a binary frame is received. The *frame* contains the data and *isLastFrame* indicates whether this is the last frame of the complete message.

This signal can be used to process large messages frame by frame, instead of waiting for the complete message to arrive.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.textFrameReceived`.
