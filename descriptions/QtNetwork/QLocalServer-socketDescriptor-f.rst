.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 7c61e48c3fd1f79ae0408fef1ff4348f

Returns the native socket descriptor the server uses to listen for incoming instructions, or -1 if the server is not listening.

The type of the descriptor depends on the platform:

* On Windows, the returned value is a `Winsock 2 Socket Handle <https://msdn.microsoft.com/en-us/library/windows/desktop/ms740522(v=vs.85).aspx>`_.

* On INTEGRITY, the returned value is the :sip:ref:`~PyQt6.QtNetwork.QTcpServer` socket descriptor and the type is defined by :sip:ref:`~PyQt6.QtNetwork.QTcpServer.socketDescriptor`.

* On all other UNIX-like operating systems, the type is a file descriptor representing a listening socket.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.listen`.
