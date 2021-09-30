.. sip:signal-description::
    :status: todo
    :pysig: 802bcd515c1808fe176128f8c5b1e839
    :realsig: (const QBluetoothServiceInfo&)
    :digest: 57dc793f574291cb733e0a86f7cd15a7

This signal is emitted when the Bluetooth service described by *info* is discovered.

**Note:** The passed :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` parameter may contain a Bluetooth Low Energy service if the target device advertises the service via SDP. This is required from device which support both, classic Bluetooth (BaseRate) and Low Energy services.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.coreConfigurations`.
