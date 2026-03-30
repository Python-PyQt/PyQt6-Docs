.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 16108e0abb2d762bd464edea647a1982

Sets the server name that will be used during the HTTP handshake phase to the given *serverName*. The *serverName* can be empty, in which case an empty server name will be sent to the client. Existing connected clients will not be notified of this change, only newly connecting clients will see this new name.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.serverName`.
