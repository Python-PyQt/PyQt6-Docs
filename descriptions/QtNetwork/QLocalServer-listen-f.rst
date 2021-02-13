.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: dca2fa1b61635326ef0bf8c35a114dc7

Tells the server to listen for incoming connections on *name*. If the server is currently listening then it will return false. Return true on success otherwise false.

*name* can be a single name and :sip:ref:`~PyQt6.QtNetwork.QLocalServer` will determine the correct platform specific path. :sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverName` will return the name that is passed into listen.

Usually you would just pass in a name like "foo", but on Unix this could also be a path such as "/tmp/foo" and on Windows this could be a pipe path such as "\\\\.\\pipe\\foo"

**Note:** On Unix if the server crashes without closing listen will fail with AddressInUseError. To create a new server the file should be removed. On Windows two local servers can listen to the same pipe at the same time, but any connections will go to one of the server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverName`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.isListening`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.close`.
