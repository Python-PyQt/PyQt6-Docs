.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 012fbeefec35bd77cf88482c5ec0a785

Attempts to close the socket. If there is pending data waiting to be written, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` will enter :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ClosingState` and wait until all data has been written. Eventually, it will enter :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.UnconnectedState` and emit the disconnectedFromServer() signal.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connectToServer`.
