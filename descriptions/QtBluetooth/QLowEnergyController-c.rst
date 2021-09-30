.. sip:class-description::
    :status: todo
    :brief: Access to Bluetooth Low Energy Devices
    :digest: 6755a949be1aba2981f7a145652542e6

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController` class provides access to Bluetooth Low Energy Devices.

:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController` acts as the entry point for Bluetooth Low Energy development.

Bluetooth Low Energy defines two types of devices; the peripheral and the central. Each role performs a different task. The peripheral device provides data which is utilized by central devices. An example might be a humidity sensor which measures the moisture in a winter garden. A device such as a mobile phone might read the sensor's value and display it to the user in the greater context of all sensors in the same environment. In this case the sensor is the peripheral device and the mobile phone acts as the central device.

A controller in the central role is created via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createCentral` factory method. Such an object essentially acts as a placeholder towards a remote Low Energy peripheral device, enabling features such as service discovery and state tracking.

After having created a controller object in the central role, the first step is to establish a connection via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectToDevice`. Once the connection has been established, the controller's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.state` changes to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.ControllerState.ConnectedState` and the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connected` signal is emitted. It is important to mention that some platforms such as a BlueZ based Linux cannot maintain two connected instances of `QLowEnergyController <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycontroller>`_ to the same remote device. In such cases the second call to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectToDevice` may fail. This limitation may disappear at some stage in the future. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.disconnectFromDevice` function is used to break the existing connection.

The second step after establishing the connection is to discover the services offered by the remote peripheral device. This process is started via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.discoverServices` and has finished once the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.discoveryFinished` signal has been emitted. The discovered services can be enumerated via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.services`.

The last step is to create service objects. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createServiceObject` function acts as factory for each service object and expects the service UUID as parameter. The calling context should take ownership of the returned `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_ instance.

Any `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_, `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_ or `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_ instance which is later created from this controller's connection becomes invalid as soon as the controller disconnects from the remote Bluetooth Low Energy device.

A controller in the peripheral role is created via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createPeripheral` factory method. Such an object acts as a peripheral device itself, enabling features such as advertising services and allowing clients to get notified about changes to characteristic values.

After having created a controller object in the peripheral role, the first step is to populate the set of GATT services offered to client devices via calls to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.addService`. Afterwards, one would call :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising` to let the device broadcast some data and, depending on the type of advertising being done, also listen for incoming connections from GATT clients.

.. seealso:: `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_, `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_, `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingParameters`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData`.
