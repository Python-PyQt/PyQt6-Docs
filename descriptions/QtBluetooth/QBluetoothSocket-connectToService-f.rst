.. sip:method-description::
    :status: todo
    :pysig: dc994d3a1d9e46b5cee52585bdfa20c3
    :realsig: (const QBluetoothServiceInfo&,QIODeviceBase::OpenMode)
    :digest: fab7096702a4202fa18ae191dbc4007e

Attempts to connect to the service described by *service*.

The socket is opened in the given *openMode*. The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.socketType` is ignored if *service* specifies a differing :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.socketProtocol`.

The socket first enters :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ConnectingState` and attempts to connect to the device providing *service*. If a connection is established, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` enters :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connected`.

At any point, the socket can emit :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.errorOccurred` to signal that an error occurred.

Note that most platforms require a pairing prior to connecting to the remote device. Otherwise the connection process may fail.

On Android, only RFCOMM connections are possible. This function ignores any socket protocol indicator and assumes RFCOMM.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.state`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnectFromService`.
