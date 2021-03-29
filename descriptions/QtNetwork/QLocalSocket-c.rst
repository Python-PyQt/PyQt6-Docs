.. sip:class-description::
    :status: todo
    :brief: Local socket
    :digest: ee81c06b5da71b2cc40879505d586b66

The :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` class provides a local socket.

On Windows this is a named pipe and on Unix this is a local domain socket.

If an error occurs, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.error` returns the type of error, and errorString() can be called to get a human readable description of what happened.

Although :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` is designed for use with an event loop, it's possible to use it without one. In that case, you must use :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForConnected`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForReadyRead`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForBytesWritten`, and :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForDisconnected` which blocks until the operation is complete or the timeout expires.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer`.
