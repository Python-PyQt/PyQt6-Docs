.. sip:method-description::
    :status: todo
    :pysig: 9daeab2db5574297592cfe242f3e4da3
    :realsig: () const
    :digest: 63eb710335ed53ae4a7fb34a4f9a648d

Returns the native socket descriptor the server uses to listen for incoming instructions, or -1 if the server is not listening.

The type of the descriptor depends on the platform:

* On Windows, the returned value is a Winsock 2 Socket Handle.

* On INTEGRITY, the returned value is the :sip:ref:`~PyQt6.QtNetwork.QTcpServer` socket descriptor and the type is defined by :sip:ref:`~PyQt6.QtNetwork.QTcpServer.socketDescriptor`.

* On all other UNIX-like operating systems, the type is a file descriptor representing a listening socket.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.listen`.
