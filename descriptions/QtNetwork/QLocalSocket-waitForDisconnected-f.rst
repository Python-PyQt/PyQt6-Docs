.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: f38d8c11ac4ae1a062b4d34c7b1b7af7

Waits until the socket has disconnected, up to *msecs* milliseconds. If the connection was successfully disconnected, this function returns ``true``; otherwise it returns ``false`` (if the operation timed out, if an error occurred, or if this :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` is already disconnected). In the case where it returns ``false``, you can call :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.error` to determine the cause of the error.

The following example waits up to one second for a connection to be closed:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_socket_qlocalsocket_unix.py
    :lines: 61-65

If *msecs* is -1, this function will not time out.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.disconnectFromServer`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.close`.
