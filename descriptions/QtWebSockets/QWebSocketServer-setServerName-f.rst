.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 16108e0abb2d762bd464edea647a1982

Sets the server name that will be used during the HTTP handshake phase to the given *serverName*. The *serverName* can be empty, in which case an empty server name will be sent to the client. Existing connected clients will not be notified of this change, only newly connecting clients will see this new name.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.serverName`.
