.. sip:method-description::
    :status: todo
    :pysig: 9daeab2db5574297592cfe242f3e4da3
    :realsig: (quintptr)
    :digest: 82f5ee0c6b08e0ea879e0a006f918b1f

This virtual function is called by :sip:ref:`~PyQt6.QtNetwork.QLocalServer` when a new connection is available. *socketDescriptor* is the native socket descriptor for the accepted connection.

The base implementation creates a :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`, sets the socket descriptor and then stores the :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` in an internal list of pending connections. Finally :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection` is emitted.

Reimplement this function to alter the server's behavior when a connection is available.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.nextPendingConnection`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.setSocketDescriptor`.
