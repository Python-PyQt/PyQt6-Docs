.. sip:class-description::
    :status: todo
    :brief: Enables connection to a Bluetooth device running a bluetooth server
    :digest: 57b8e8a17cc10dc24b0cb83eaadbee76

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` class enables connection to a Bluetooth device running a bluetooth server.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` supports two socket types, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol.L2capProtocol` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol.RfcommProtocol`.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol.L2capProtocol` is a low level datagram-oriented Bluetooth socket. Android does not support :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol.L2capProtocol` for socket connections.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol.RfcommProtocol` is a reliable, stream-oriented socket. RFCOMM sockets emulate an RS-232 serial port.

To create a connection to a Bluetooth service, create a socket of the appropriate type and call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connectToService` passing the Bluetooth address and port number. :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` will emit the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connected` signal when the connection is established.

If the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol` is not supported on a platform, calling :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connectToService` will emit a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketError.UnsupportedProtocolError` error.

**Note:** :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` does not support synchronous read and write operations. Functions such as waitForReadyRead() and waitForBytesWritten() are not implemented. I/O operations should be performed using readyRead(), read() and write().

On iOS, this class cannot be used because the platform does not expose an API which may permit access to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` related features.
