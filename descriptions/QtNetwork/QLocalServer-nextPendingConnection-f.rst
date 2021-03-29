.. sip:method-description::
    :status: todo
    :pysig: db2018af6e33b41f2444c94fd7fdc8c7
    :realsig: ()
    :digest: c087aaa68f3d7e58ff28f7763bd6d1f1

Returns the next pending connection as a connected :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` object.

The socket is created as a child of the server, which means that it is automatically deleted when the :sip:ref:`~PyQt6.QtNetwork.QLocalServer` object is destroyed. It is still a good idea to delete the object explicitly when you are done with it, to avoid wasting memory.

``nullptr`` is returned if this function is called when there are no pending connections.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.hasPendingConnections`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.incomingConnection`.
