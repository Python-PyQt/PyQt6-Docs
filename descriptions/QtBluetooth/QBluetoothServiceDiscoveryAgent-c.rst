.. sip:class-description::
    :status: todo
    :brief: Enables you to query for Bluetooth services
    :digest: 8aad721610c5a460fb58ee1278da6fc3

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent` class enables you to query for Bluetooth services.

The discovery process relies on the Bluetooth Service Discovery Process (SDP). The following steps are required to query the services provided by all contactable Bluetooth devices:

* create an instance of :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent`,

* connect to either the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.serviceDiscovered` or :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.finished` signals,

* and call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.start`.

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-doc-snippets-doc_src_qtbluetooth.py
    :lines: 138-157

By default a minimal service discovery is performed. In this mode, the returned :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` objects are guaranteed to contain only device and service UUID information. Depending on platform and device capabilities, other service information may also be available. The minimal service discovery mode relies on cached SDP data of the platform. Therefore it is possible that this discovery does not find a device although it is physically available. In such cases a full discovery must be performed to force an update of the platform cache. However for most use cases a minimal discovery is adequate as it is much quicker and other classes which require up-to-date information such as :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.connectToService` will perform additional discovery if required. If the full service information is required, pass :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode.FullDiscovery` as the discoveryMode parameter to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.start`.

This class may internally utilize `QBluetoothDeviceDiscoveryAgent <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qbluetoothdevicediscoveryagent>`_ to find unknown devices.

The service discovery may find Bluetooth Low Energy services too if the target device is a combination of a classic and Low Energy device. Those devices are required to advertise their Low Energy services via SDP. If the target device only supports Bluetooth Low Energy services, it is likely to not advertise them via SDP. The `QLowEnergyController <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycontroller>`_ class should be utilized to perform the service discovery on Low Energy devices.

On iOS, this class cannot be used because the platform does not expose an API which may permit access to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent` related features.

.. seealso:: `QBluetoothDeviceDiscoveryAgent <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qbluetoothdevicediscoveryagent>`_, `QLowEnergyController <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycontroller>`_.
