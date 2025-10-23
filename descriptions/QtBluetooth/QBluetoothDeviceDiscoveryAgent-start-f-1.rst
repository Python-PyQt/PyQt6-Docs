.. sip:method-description::
    :status: todo
    :pysig: d515832d732b94d87ef7f58a977c5622
    :realsig: (QBluetoothDeviceDiscoveryAgent::DiscoveryMethods)
    :digest: c9ef25837ff5d108ec5c3b2669af58fa

Starts Bluetooth device discovery, if it is not already started and the provided *methods* are supported. The discovery *methods* limit the scope of the device search. For example, if the target service or device is a Bluetooth Low Energy device, this function could be used to limit the search to Bluetooth Low Energy devices and thereby reduces the discovery time significantly.

**Note:** *methods* only determines the type of discovery and does not imply the filtering of the results. For example, the search may still contain classic bluetooth devices despite *methods* being set to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod.LowEnergyMethod` only. This may happen due to previously cached search results which may be incorporated into the search results.

**Note:** Some platforms (e.g. Windows) may also provide cached results for the devices that are not currently advertising. Other platforms (like ``iOS``) only provide information about currently advertising devices. You can store the received device UUID (or Bluetooth address) upon first discovery, and then use it later to establish a connection directly (see QBluetoothDeviceInfo). This way the applications can omit the later device discovery phases. Using the Bluetooth address requires that the remote device's Bluetooth address does not change.
