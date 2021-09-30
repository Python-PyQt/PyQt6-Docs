.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 54dd31064219fd119b4a70bc02d74d80

Starts Bluetooth device discovery, if it is not already started.

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.deviceDiscovered` signal is emitted as each device is discovered. The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished` signal is emitted once device discovery is complete. The discovery utilizes the maximum set of supported discovery methods on the platform.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.supportedDiscoveryMethods`.
