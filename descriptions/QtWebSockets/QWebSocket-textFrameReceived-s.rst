.. sip:signal-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&,bool)
    :digest: 2424e7383d01458ec4d3a0a819a48445

This signal is emitted whenever a text frame is received. The *frame* contains the data and *isLastFrame* indicates whether this is the last frame of the complete message.

This signal can be used to process large messages frame by frame, instead of waiting for the complete message to arrive.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.binaryFrameReceived`.
