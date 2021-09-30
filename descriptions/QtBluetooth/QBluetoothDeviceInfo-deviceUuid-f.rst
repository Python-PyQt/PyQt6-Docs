.. sip:method-description::
    :status: todo
    :pysig: f5a13b3bac878820b76483c7239f5b8c
    :realsig: () const
    :digest: adda16b341b2f98ac55035e4f5b209ff

Returns a unique identifier for a Bluetooth device without an address.

In general, this uuid is invalid on every platform but macOS and iOS. It is used as a workaround for those two platforms as they do not provide Bluetooth addresses for found Bluetooth Low Energy devices. Every other platform uses :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.address` instead.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.setDeviceUuid`.
