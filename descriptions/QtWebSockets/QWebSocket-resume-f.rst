.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 90a26a3542f6922e4115cd9e39ff8431

Continues data transfer on the socket. This method should only be used after the socket has been set to pause upon notifications and a notification has been received. The only notification currently supported is :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslErrors`. Calling this method if the socket is not paused results in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.pauseMode`, :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.setPauseMode`.
