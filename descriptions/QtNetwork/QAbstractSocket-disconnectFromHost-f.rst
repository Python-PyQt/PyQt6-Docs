.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1c628bf9567f209591770e0a8f025042

Attempts to close the socket. If there is pending data waiting to be written, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` will enter :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ClosingState` and wait until all data has been written. Eventually, it will enter :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.UnconnectedState` and emit the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnected` signal.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`.
