.. sip:method-description::
    :status: todo
    :pysig: a003bf5ba9a9b5d775b6491a780a8cab
    :realsig: (qintptr,QAbstractSocket::SocketState,QIODeviceBase::OpenMode)
    :digest: 1a3fe268a9ba8a8efb5cded7ca0afead

Initializes :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` with the native socket descriptor *socketDescriptor*. Returns ``true`` if *socketDescriptor* is accepted as a valid socket descriptor; otherwise returns ``false``. The socket is opened in the mode specified by *openMode*, and enters the socket state specified by *socketState*. Read and write buffers are cleared, discarding any pending data.

**Note:** It is not possible to initialize two abstract sockets with the same native socket descriptor.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.socketDescriptor`.
