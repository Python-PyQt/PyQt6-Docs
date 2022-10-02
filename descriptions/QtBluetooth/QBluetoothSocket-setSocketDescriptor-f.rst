.. sip:method-description::
    :status: todo
    :pysig: 99178bef63060276e4f87e00c0b549ca
    :realsig: (int,QBluetoothServiceInfo::Protocol,QBluetoothSocket::SocketState,QIODeviceBase::OpenMode)
    :digest: 2512ed07ae212e1e14743e5c48a2d3f3

Sets the socket to use *socketDescriptor* with a type of *socketType*, which is in state *socketState*, and mode *openMode*.

The socket descriptor is owned by the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket` instance and may be closed once finished.

Returns ``true`` on success.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.socketDescriptor`.
