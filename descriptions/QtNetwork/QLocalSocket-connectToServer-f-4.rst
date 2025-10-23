.. sip:method-description::
    :status: todo
    :pysig: db9e987ef4095603eb9a90fba7ad8846
    :realsig: (const QString&, QIODeviceBase::OpenMode)
    :digest: 47a5a06caea120f503949b516b859d73

Set the server *name* and attempts to make a connection to it.

The socket is opened in the given *openMode* and first enters :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectingState`. If a connection is established, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` enters :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connected`.

After calling this function, the socket can emit :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.errorOccurred` to signal that an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.state`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.serverName`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForConnected`.
