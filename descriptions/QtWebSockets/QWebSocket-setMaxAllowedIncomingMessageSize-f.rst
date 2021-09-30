.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint64)
    :digest: 3d81afb4e3b9b91ac8dd726f4d31613c

Sets the maximum allowed size of an incoming websocket message to *maxAllowedIncomingMessageSize*. If an incoming message exceeds this limit, the peer gets disconnected. The accepted range is between 0 and :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxIncomingMessageSize`, default is :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxIncomingMessageSize`. The purpose of this function is to avoid exhausting virtual memory.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxAllowedIncomingMessageSize`.
