.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8cd2806723f48595db6b5a4d3d7ce4a0

Attempts to close the socket. If there is pending data waiting to be written :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` will enter :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.ClosingState` and wait until all data has been written. Eventually, it will enter :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.SocketState.UnconnectedState` and emit the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnected` signal.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connectToService`.
