.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint64)
    :digest: 70a5adb3b9577f4411ef93b095d47d93

Sets the maximum size of an outgoing websocket frame to *outgoingFrameSize*. The accepted range is between 0 and :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.maxOutgoingFrameSize`, default is 512kB. The purpose of this function is to adapt to the maximum allowed frame size of the receiver.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.outgoingFrameSize`.
