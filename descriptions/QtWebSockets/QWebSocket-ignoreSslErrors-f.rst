.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 96b7e6df2a483f5faa3762c07f927e97

This slot tells :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` to ignore errors during :sip:ref:`~PyQt6.QtWebSockets.QWebSocket`'s handshake phase and continue connecting. If you want to continue with the connection even if errors occur during the handshake phase, then you must call this slot, either from a slot connected to :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslErrors`, or before the handshake phase. If you don't call this slot, either in response to errors or before the handshake, the connection will be dropped after the :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslErrors` signal has been emitted.

**Warning:** Be sure to always let the user inspect the errors reported by the :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslErrors` signal, and only call this method upon confirmation from the user that proceeding is ok. If there are unexpected errors, the connection should be aborted. Calling this method without inspecting the actual errors will most likely pose a security risk for your application. Use it with great care!

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors`.
