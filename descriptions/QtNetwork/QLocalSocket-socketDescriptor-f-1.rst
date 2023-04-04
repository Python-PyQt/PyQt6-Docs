.. sip:method-description::
    :status: todo
    :pysig: 9daeab2db5574297592cfe242f3e4da3
    :realsig: () const
    :digest: fd0150af0bdfc67630e0ac66f436d6c3

Returns the native socket descriptor of the :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` object if this is available; otherwise returns -1.

The socket descriptor is not available when :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` is in :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.UnconnectedState`. The type of the descriptor depends on the platform:

* On Windows, the returned value is a Winsock 2 Socket Handle.

* On INTEGRITY, the returned value is the :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` socket descriptor and the type is defined by socketDescriptor.

* On all other UNIX-like operating systems, the type is a file descriptor representing a socket.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.setSocketDescriptor`.
