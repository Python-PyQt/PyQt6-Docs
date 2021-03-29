.. sip:method-description::
    :status: todo
    :pysig: fa9607d7c74348deaea2550ae89b9113
    :realsig: ()
    :digest: ec695e0501fb25f510478e60172e4ab3

Returns the next pending connection as a connected :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` object.

The socket is created as a child of the server, which means that it is automatically deleted when the :sip:ref:`~PyQt6.QtNetwork.QTcpServer` object is destroyed. It is still a good idea to delete the object explicitly when you are done with it, to avoid wasting memory.

``nullptr`` is returned if this function is called when there are no pending connections.

**Note:** The returned :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` object cannot be used from another thread. If you want to use an incoming connection from another thread, you need to override :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.hasPendingConnections`.
