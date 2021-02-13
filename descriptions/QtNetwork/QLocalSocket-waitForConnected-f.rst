.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: 16fda9db527dc651138538df7be037a0

Waits until the socket is connected, up to *msecs* milliseconds. If the connection has been established, this function returns ``true``; otherwise it returns ``false``. In the case where it returns ``false``, you can call :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.error` to determine the cause of the error.

The following example waits up to one second for a connection to be established:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_socket_qlocalsocket_unix.py
    :lines: 54-56

If *msecs* is -1, this function will not time out.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connectToServer`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connected`.
