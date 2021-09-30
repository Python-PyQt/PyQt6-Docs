.. sip:method-description::
    :status: todo
    :pysig: 7061bd563dd6f05f08d6801695e91e5e
    :realsig: (qintptr)
    :digest: 1785e9704a6b549656a85e7d105812ab

Sets the socket descriptor this server should use when listening for incoming connections to *socketDescriptor*.

Returns true if the socket is set successfully; otherwise returns false. The socket is assumed to be in listening state.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.socketDescriptor`, :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.isListening`.
