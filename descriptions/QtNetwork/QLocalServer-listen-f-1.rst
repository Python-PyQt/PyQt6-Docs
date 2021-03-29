.. sip:method-description::
    :status: todo
    :pysig: 7061bd563dd6f05f08d6801695e91e5e
    :realsig: (qintptr)
    :digest: 7d4698bf5008786f75e4562344f6f06f

Instructs the server to listen for incoming connections on *socketDescriptor*. The property returns ``false`` if the server is currently listening. It returns ``true`` on success; otherwise, it returns ``false``. The socket must be ready to accept new connections with no extra platform-specific functions called. The socket is set into non-blocking mode.

:sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverName`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.fullServerName` may return a string with a name if this option is supported by the platform; otherwise, they return an empty QString.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.isListening`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.close`.
