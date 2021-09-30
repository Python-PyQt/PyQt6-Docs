.. sip:method-description::
    :status: todo
    :pysig: e1a34a46ed2db7698c347df56279a312
    :realsig: (QLowEnergyController::RemoteAddressType)
    :digest: cd09bc1f43efc4cca14b70d371d7b52b

Sets the remote address *type*. The type is required to connect to the remote Bluetooth Low Energy device.

This attribute is only required to be set on Linux/BlueZ systems with older Linux kernels (v3.3 or lower), or if CAP_NET_ADMIN is not set for the executable. The default value of the attribute is :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.RemoteAddressType.RandomAddress`.

**Note:** All other platforms handle this flag transparently and therefore applications can ignore it entirely. On Linux, the address type flag is not directly exposed by BlueZ although some use cases do require this information. The only way to detect the flag is via the Linux kernel's Bluetooth Management API (kernel version 3.4+ required). This API requires CAP_NET_ADMIN capabilities though. If the local :sip:ref:`~PyQt6.QtBluetooth` process has this capability set :sip:ref:`~PyQt6.QtBluetooth` will use the API. This assumes that `QBluetoothDeviceDiscoveryAgent <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qbluetoothdevicediscoveryagent>`_ was used prior to calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectToDevice`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.remoteAddressType`.
