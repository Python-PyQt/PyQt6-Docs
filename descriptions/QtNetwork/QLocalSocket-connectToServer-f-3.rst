.. sip:method-description::
    :status: todo
    :pysig: abcdcf2a50cef5b42db271b38c126250
    :realsig: (const QString&,QIODeviceBase::OpenMode)
    :digest: e0b596098f7c7bb1f6e9984e15ed0450

This is an overloaded function.

Set the server *name* and attempts to make a connection to it.

The socket is opened in the given *openMode* and first enters :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectingState`. If a connection is established, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` enters :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connected`.

After calling this function, the socket can emit :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.errorOccurred` to signal that an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.state`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.serverName`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForConnected`.
