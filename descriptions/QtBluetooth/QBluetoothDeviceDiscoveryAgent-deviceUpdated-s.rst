.. sip:signal-description::
    :status: todo
    :pysig: 8d7c9d0d571ab1ac4082a501fd84f0f5
    :realsig: (const QBluetoothDeviceInfo&,QBluetoothDeviceInfo::Fields)
    :digest: 54fc93f7f652b39750b2ebf4cfcd96ca

This signal is emitted when the agent receives additional information about the Bluetooth device described by *info*. The *updatedFields* flags tell which information has been updated.

During discovery, some information can change dynamically, such as :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.rssi` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.manufacturerData`. This signal informs you that if your application is displaying this data, it can be updated, rather than waiting until the discovery has finished.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.rssi`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.lowEnergyDiscoveryTimeout`.
