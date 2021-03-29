.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: e5449498255f022b9407a4dab5ccc38e

Waits until the socket is connected, up to *msecs* milliseconds. If the connection has been established, this function returns ``true``; otherwise it returns ``false``. In the case where it returns ``false``, you can call :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.error` to determine the cause of the error.

The following example waits up to one second for a connection to be established:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_socket_qabstractsocket.py
    :lines: 54-56

If msecs is -1, this function will not time out.

**Note:** This function may wait slightly longer than *msecs*, depending on the time it takes to complete the host lookup.

**Note:** Multiple calls to this functions do not accumulate the time. If the function times out, the connecting process will be aborted.

**Note:** This function may fail randomly on Windows. Consider using the event loop and the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected` signal if your software will run on Windows.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected`.
