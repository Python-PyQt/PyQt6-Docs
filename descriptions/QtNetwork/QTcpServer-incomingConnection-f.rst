.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: (qintptr)
    :digest: f6123b64a2f3ee8dcba2bc814a2cfe13

This virtual function is called by :sip:ref:`~PyQt6.QtNetwork.QTcpServer` when a new connection is available. The *socketDescriptor* argument is the native socket descriptor for the accepted connection.

The base implementation creates a :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, sets the socket descriptor and then stores the :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` in an internal list of pending connections. Finally :sip:ref:`~PyQt6.QtNetwork.QTcpServer.newConnection` is emitted.

Reimplement this function to alter the server's behavior when a connection is available.

If this server is using :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` then the *socketDescriptor* may not be usable with native socket functions, and should only be used with QTcpSocket::setSocketDescriptor().

**Note:** If another socket is created in the reimplementation of this method, it needs to be added to the Pending Connections mechanism by calling :sip:ref:`~PyQt6.QtNetwork.QTcpServer.addPendingConnection`.

**Note:** If you want to handle an incoming connection as a new :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` object in another thread you have to pass the :sip:ref:`~PyQt6.QtNetwork.QTcpServer.socketDescriptor` to the other thread and create the :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` object there and use its :sip:ref:`~PyQt6.QtNetwork.QTcpServer.setSocketDescriptor` method.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.newConnection`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer.nextPendingConnection`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer.addPendingConnection`.
