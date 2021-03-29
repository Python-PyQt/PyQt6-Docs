.. sip:method-description::
    :status: todo
    :pysig: 53f67762c018ef3e3feef56f0bb203e8
    :realsig: (const QString&,quint16,QIODeviceBase::OpenMode,QAbstractSocket::NetworkLayerProtocol)
    :digest: 504c3cf0e4da5f363f219cd6d002ea42

Attempts to make a connection to *hostName* on the given *port*. The *protocol* parameter can be used to specify which network protocol to use (eg. IPv4 or IPv6).

The socket is opened in the given *openMode* and first enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.HostLookupState`, then performs a host name lookup of *hostName*. If the lookup succeeds, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.hostFound` is emitted and :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectingState`. It then attempts to connect to the address or addresses returned by the lookup. Finally, if a connection is established, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected`.

At any point, the socket can emit :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.errorOccurred` to signal that an error occurred.

*hostName* may be an IP address in string form (e.g., "43.195.83.32"), or it may be a host name (e.g., "example.com"). :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` will do a lookup only if required. *port* is in native byte order.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.state`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerName`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerPort`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.waitForConnected`.
