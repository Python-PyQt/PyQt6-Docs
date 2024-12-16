.. sip:method-description::
    :status: todo
    :pysig: f1e0f40f3e812dcd0f5bb972e78b9b43
    :realsig: () const
    :digest: bbb29ad9863a0776f8450d31341952ca

Returns the list of connected devices. This list is different from the list of currently paired devices.

On Android and macOS, it is not possible to retrieve a list of connected devices. It is only possible to listen to (dis)connect changes. For convenience, this class monitors all connect and disconnect events since its instanciation and returns the current list when calling this function. Therefore it is possible that this function returns an empty list shortly after creating an instance.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.deviceConnected`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.deviceDisconnected`.
