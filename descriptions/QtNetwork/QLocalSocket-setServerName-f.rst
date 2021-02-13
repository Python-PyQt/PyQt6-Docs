.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: f34140829c4adcc39b8b60c9a658f92b

Set the *name* of the peer to connect to. On Windows name is the name of a named pipe; on Unix name is the name of a local domain socket.

This function must be called when the socket is not connected.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.serverName`.
