.. sip:method-description::
    :status: todo
    :pysig: 08d90ad23770ac9b463b9a98f8c42a16
    :realsig: (const QBluetoothAddress&,quint16,QIODeviceBase::OpenMode)
    :digest: a120f8931b7fd2d2de8190931fc97aed

Attempts to make a connection with *address* on the given *port*.

The socket is opened in the given *openMode*.

The socket first enters :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ConnectingState`, and attempts to connect to *address*. If a connection is established, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` enters :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connected`.

At any point, the socket can emit :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.error` to signal that an error occurred.

On Android and BlueZ (version 5.46 or above), a connection to a service can not be established using a port. Calling this function will emit a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketError.ServiceNotFoundError`.

Note that most platforms require a pairing prior to connecting to the remote device. Otherwise the connection process may fail.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.state`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnectFromService`.
