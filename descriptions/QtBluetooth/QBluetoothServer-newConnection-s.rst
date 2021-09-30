.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 510fb240d45a2353501a73dff9c04a9c

This signal is emitted when a new connection is available.

The connected slot should call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.nextPendingConnection` to get a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` object to send and receive data over the connection.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.nextPendingConnection`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.hasPendingConnections`.
