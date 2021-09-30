.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 569792fc93e2dc07796d64606038a91d

This signal is emitted when the Bluetooth service discovery completes.

Unlike the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished` signal this signal will even be emitted when an error occurred during the service discovery. Therefore it is recommended to check the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.error` signal to evaluate the success of the service discovery discovery.
