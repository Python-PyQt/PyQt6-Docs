.. sip:method-description::
    :status: todo
    :pysig: 58a762c3837c351e88a36a644fee575a
    :realsig: (qintptr)
    :digest: 0e6f0f7116c7aa457bbd28f2dd28ce99

Sets the socket descriptor this server should use when listening for incoming connections to *socketDescriptor*. Returns ``true`` if the socket is set successfully; otherwise returns ``false``.

The socket is assumed to be in listening state.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.socketDescriptor`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer.isListening`.
