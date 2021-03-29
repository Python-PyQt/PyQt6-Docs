.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: 3d220bcf7988c38d42a5b12260f62907

Waits until the socket has disconnected, up to *msecs* milliseconds. If the connection was successfully disconnected, this function returns ``true``; otherwise it returns ``false`` (if the operation timed out, if an error occurred, or if this :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` is already disconnected). In the case where it returns ``false``, you can call :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.error` to determine the cause of the error.

The following example waits up to one second for a connection to be closed:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_socket_qabstractsocket.py
    :lines: 61-65

If msecs is -1, this function will not time out.

**Note:** This function may fail randomly on Windows. Consider using the event loop and the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnected` signal if your software will run on Windows.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnectFromHost`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.close`.
