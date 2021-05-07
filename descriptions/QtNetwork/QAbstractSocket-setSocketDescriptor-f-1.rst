.. sip:method-description::
    :status: todo
    :pysig: 5a72e06b88c2ea70be308a9880111ed8
    :realsig: (qintptr,QAbstractSocket::SocketState,QIODeviceBase::OpenMode)
    :digest: 1a3fe268a9ba8a8efb5cded7ca0afead

Initializes :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` with the native socket descriptor *socketDescriptor*. Returns ``true`` if *socketDescriptor* is accepted as a valid socket descriptor; otherwise returns ``false``. The socket is opened in the mode specified by *openMode*, and enters the socket state specified by *socketState*. Read and write buffers are cleared, discarding any pending data.

**Note:** It is not possible to initialize two abstract sockets with the same native socket descriptor.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.socketDescriptor`.
