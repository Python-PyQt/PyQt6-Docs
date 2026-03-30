.. sip:method-description::
    :status: todo
    :pysig: 502f7d3e77c89e5ef63bfbd42eaccbfd
    :realsig: (const QString&)
    :digest: a104d7bb849faeccbce0023e44261e9b

Tells the server to listen for incoming connections on *name*. If the server is already listening, listen() will fail. Returns ``true`` on success, ``false`` otherwise.

*name* can be a single name and :sip:ref:`~PyQt6.QtNetwork.QLocalServer` will determine the correct platform specific path. :sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverName` will return the name that was passed into listen().

Usually you would just pass in a name like "foo", but on Unix this could also be a path such as "/tmp/foo" and on Windows this could be a pipe path such as "\\\\.``\pipe````\foo``"

**Note:** On Unix, if the server previously crashed without closing, listen() will fail with AddressInUseError. To create a new server, the file should first be removed. On Windows, two local servers can listen to the same pipe at the same time, but each incoming connection will go to any one of them.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverName`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.isListening`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.close`.
