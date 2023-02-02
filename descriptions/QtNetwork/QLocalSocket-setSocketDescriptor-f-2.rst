.. sip:method-description::
    :status: todo
    :pysig: f78f2940860071c57de26f3d44acdd04
    :realsig: (qintptr,QLocalSocket::LocalSocketState,QIODeviceBase::OpenMode)
    :digest: 5cc709dc2891af65edc0bf93c035d1a0

Initializes :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` with the native socket descriptor *socketDescriptor*. Returns ``true`` if :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.socketDescriptor` is accepted as a valid socket descriptor; otherwise returns ``false``. The socket is opened in the mode specified by *openMode*, and enters the socket state specified by *socketState*.

**Note:** It is not possible to initialize two local sockets with the same native socket descriptor.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.socketDescriptor`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.state`, openMode().
