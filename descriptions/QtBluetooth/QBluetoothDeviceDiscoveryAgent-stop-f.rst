.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0e61b0d2309ad09a2adc0e97a031aee6

Stops Bluetooth device discovery. The cancel() signal is emitted once the device discovery is canceled. :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.start` maybe called before the cancel signal is received. Once :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.start` has been called the cancel signal from the prior discovery will be discarded.
