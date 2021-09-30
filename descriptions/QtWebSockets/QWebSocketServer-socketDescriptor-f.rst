.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 01db07e6a78f8425efce64e728cd5c26

Returns the native socket descriptor the server uses to listen for incoming instructions, or -1 if the server is not listening. If the server is using :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`, the returned descriptor may not be usable with native socket functions.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.setSocketDescriptor`, :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.isListening`.
