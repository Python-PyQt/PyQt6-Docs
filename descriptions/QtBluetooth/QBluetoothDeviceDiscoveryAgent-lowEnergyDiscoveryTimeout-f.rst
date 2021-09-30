.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 319f04a523567470f3a1d065405f5617

Returns a timeout in milliseconds that is applied to the Bluetooth Low Energy device search. A value of ``-1`` implies that the platform does not support this property and the timeout for the device search cannot be adjusted. A return value of ``0`` implies a never-ending search which must be manually stopped via :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.stop`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.setLowEnergyDiscoveryTimeout`.
