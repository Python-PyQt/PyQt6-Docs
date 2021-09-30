.. sip:signal-description::
    :status: todo
    :pysig: 5fe13b99212ab2dd3d7dd89f7b316c94
    :realsig: (const QBluetoothDeviceInfo&)
    :digest: d102c0fe86c1d59f15d4ae6b6291716f

This signal is emitted when the Bluetooth device described by *info* is discovered.

The signal is emitted as soon as the most important device information has been collected. However, as long as the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished` signal has not been emitted the information collection continues even for already discovered devices. This is particularly true for signal strength information (RSSI) and manufacturer data updates. If the use case requires continuous manufacturer data or RSSI updates it is advisable to retrieve the device information via :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.discoveredDevices` once the discovery has finished or listen to the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.deviceUpdated` signal.

If :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.lowEnergyDiscoveryTimeout` is larger than 0 the signal is only ever emitted when at least one attribute of *info* changes. This reflects the desire to receive updates as more precise information becomes available. The exception to this behavior is the case when :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.lowEnergyDiscoveryTimeout` is set to ``0``. A timeout of ``0`` expresses the desire to monitor the appearance and disappearance of Low Energy devices over time. Under this condition the deviceDiscovered() signal is emitted even if *info* has not changed since the last signal emission.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.rssi`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.lowEnergyDiscoveryTimeout`.
