.. sip:class-description::
    :status: todo
    :brief: Discovers the Bluetooth devices nearby
    :digest: 7e1194e64fda713f8829ee5c19efe28a

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent` class discovers the Bluetooth devices nearby.

To discover the nearby Bluetooth devices:

* create an instance of :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent`,

* connect to either the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.deviceDiscovered` or :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished` signals,

* and call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.start`.

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-doc-snippets-doc_src_qtbluetooth.py
    :lines: 116-134

To retrieve results asynchronously, connect to the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.deviceDiscovered` signal. To get a list of all discovered devices, call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.discoveredDevices` after the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished` signal.

This class can be used to discover Classic and Low Energy Bluetooth devices. The individual device type can be determined via the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.coreConfigurations` attribute. In most cases the list returned by :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.discoveredDevices` contains both types of devices. However not every platform can detect both types of devices. On platforms with this limitation (for example iOS only suports Low Energy discovery), the discovery process will limit the search to the type which is supported.

**Note:** Since Android 6.0 the ability to detect devices requires ACCESS_COARSE_LOCATION.

**Note:** Due to API limitations it is only possible to find devices that have been paired using Windows' settings on Windows.

**Note:** The Win32 backend currently does not support the Received Signal Strength Indicator (RSSI), as well as the Manufacturer Specific Data, or other data updates advertised by Bluetooth LE devices after discovery.
