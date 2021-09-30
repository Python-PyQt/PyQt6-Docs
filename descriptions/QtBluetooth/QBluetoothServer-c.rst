.. sip:class-description::
    :status: todo
    :brief: Uses the RFCOMM or L2cap protocol to communicate with a Bluetooth device
    :digest: 9b249f572579c3c92461bb7a142362d5

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer` class uses the RFCOMM or L2cap protocol to communicate with a Bluetooth device.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer` is used to implement Bluetooth services over RFCOMM or L2cap.

Start listening for incoming connections with :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.listen`. Wait till the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.newConnection` signal is emitted when a new connection is established, and call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.nextPendingConnection` to get a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` for the new connection.

To enable other devices to find your service, create a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` with the applicable attributes for your service and register it using :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.registerService`. Call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.serverPort` to get the channel number that is being used.

If the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol` is not supported by a platform, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.listen` will return ``false``. Android and WinRT only support RFCOMM for example.

On iOS, this class cannot be used because the platform does not expose an API which may permit access to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer` related features.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo`, `QBluetoothSocket <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qbluetoothsocket>`_.
