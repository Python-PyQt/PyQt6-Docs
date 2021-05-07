.. sip:method-description::
    :status: todo
    :pysig: 27ca050dd4a000daba88f21e2fe7f93d
    :realsig: (QIODeviceBase::OpenMode)
    :digest: 37b40f0ea3bb5ef99908f2b577671169

Attempts to make a connection to :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.serverName`. :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.setServerName` must be called before you open the connection. Alternatively you can use (const QString &name, OpenMode openMode);

The socket is opened in the given *openMode* and first enters :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectingState`. If a connection is established, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket` enters :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connected`.

After calling this function, the socket can emit :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.errorOccurred` to signal that an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.state`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.serverName`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.waitForConnected`.
