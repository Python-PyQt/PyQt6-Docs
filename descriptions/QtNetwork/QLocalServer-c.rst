.. sip:class-description::
    :status: todo
    :brief: Local socket based server
    :digest: d621ba8f9d4ac2b98d94e702b7fe055e

The :sip:ref:`~PyQt6.QtNetwork.QLocalServer` class provides a local socket based server.

This class makes it possible to accept incoming local socket connections.

Call :sip:ref:`~PyQt6.QtNetwork.QLocalServer.listen` to have the server start listening for incoming connections on a specified key. The :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection` signal is then emitted each time a client connects to the server.

Call :sip:ref:`~PyQt6.QtNetwork.QLocalServer.nextPendingConnection` to accept the pending connection as a connected :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`. The function returns a pointer to a :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` that can be used for communicating with the client.

If an error occurs, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverError` returns the type of error, and :sip:ref:`~PyQt6.QtNetwork.QLocalServer.errorString` can be called to get a human readable description of what happened.

When listening for connections, the name which the server is listening on is available through :sip:ref:`~PyQt6.QtNetwork.QLocalServer.serverName`.

Calling :sip:ref:`~PyQt6.QtNetwork.QLocalServer.close` makes :sip:ref:`~PyQt6.QtNetwork.QLocalServer` stop listening for incoming connections.

Although :sip:ref:`~PyQt6.QtNetwork.QLocalServer` is designed for use with an event loop, it's possible to use it without one. In that case, you must use :sip:ref:`~PyQt6.QtNetwork.QLocalServer.waitForNewConnection`, which blocks until either a connection is available or a timeout expires.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer`.
