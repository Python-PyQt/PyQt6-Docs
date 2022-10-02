.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cfc035613280e8c001d6ffd37e654fa2

This signal is emitted when the Bluetooth service discovery completes.

Unlike the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished` signal this signal will even be emitted when an error occurred during the service discovery. Therefore it is recommended to check the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.errorOccurred` signal to evaluate the success of the service discovery discovery.
