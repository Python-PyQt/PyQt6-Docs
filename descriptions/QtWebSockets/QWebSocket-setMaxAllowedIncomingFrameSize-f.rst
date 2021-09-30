.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint64)
    :digest: 77ee52d94cdecd54d1cd8f441d4d1577

Sets the maximum allowed size of an incoming websocket frame to *maxAllowedIncomingFrameSize*. If an incoming frame exceeds this limit, the peer gets disconnected. The accepted range is between 0 and :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxIncomingFrameSize`, default is :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxIncomingFrameSize`. The purpose of this function is to avoid exhausting virtual memory.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxAllowedIncomingFrameSize`.
