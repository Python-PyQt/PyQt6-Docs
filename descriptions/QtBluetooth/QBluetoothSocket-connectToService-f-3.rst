.. sip:method-description::
    :status: todo
    :pysig: ec2febe48b6f76c866548f14267dd112
    :realsig: (const QBluetoothAddress&,const QBluetoothUuid&,QIODeviceBase::OpenMode)
    :digest: b1efd37e99b2be68a4d50e310909a153

Attempts to make a connection to the service identified by *uuid* on the device with address *address*.

The socket is opened in the given *openMode*.

For BlueZ, the socket first enters the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ServiceLookupState` and queries the connection parameters for *uuid*. If the service parameters are successfully retrieved the socket enters :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ConnectingState`, and attempts to connect to *address*. If a connection is established, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` enters :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connected`.

On Android, the service connection can directly be established using the UUID of the remote service. Therefore the platform does not require the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ServiceLookupState` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.socketType` is always set to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol.RfcommProtocol`.

At any point, the socket can emit :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.errorOccurred` to signal that an error occurred.

Note that most platforms require a pairing prior to connecting to the remote device. Otherwise the connection process may fail.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.state`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnectFromService`.
