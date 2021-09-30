.. sip:class-description::
    :status: todo
    :brief: Represents an individual service on a Bluetooth Low Energy Device
    :digest: 7939c2a1416d643da8b084ce10386929

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` class represents an individual service on a Bluetooth Low Energy Device.

:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` provides access to the details of Bluetooth Low Energy services. The class facilitates the discovery and publification of service details, permits reading and writing of the contained data and notifies about data changes.

.. _qlowenergyservice-service-structure:

Service Structure
-----------------

A Bluetooth Low Energy peripheral device can contain multiple services. In turn each service may include further services. This class represents a single service of the peripheral device and is created via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createServiceObject`. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.type` indicates whether this service is a primary (top-level) service or whether the service is part of another service. Each service may contain one or more characteristics and each characteristic may contain descriptors. The resulting structure may look like the following diagram:

.. image:: ../../../images/peripheral-structure.png

A characteristic is the principal information carrier. It has a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.value` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.value` describing the access permissions for the value. The general purpose of the contained descriptor is to further define the nature of the characteristic. For example, it might specify how the value is meant to be interpreted or whether it can notify the value consumer about value changes.

.. _qlowenergyservice-service-interaction:

Service Interaction
-------------------

Once a service object was created for the first time, its details are yet to be discovered. This is indicated by its current :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.state` being :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveryRequired`. It is only possible to retrieve the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.serviceUuid` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.serviceName`.

The discovery of its included services, characteristics and descriptors is triggered when calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.discoverDetails`. During the discovery the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.state` transitions from :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveryRequired` via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveringService` to its final :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state. This transition is advertised via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.stateChanged` signal. Once the details are known, all of the contained characteristics, descriptors and included services are known and can be read or written.

The values of characteristics and descriptors can be retrieved via `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_ and `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_, respectively. However, direct reading or writing of these attributes requires the service object. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic` function attempts to re-read the value of a characteristic. Although the initial service discovery may have obtained a value already this call may be required in cases where the characteristic value constantly changes without any notifications being provided. An example might be a time characteristic that provides a continuous value. If the read attempt is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicRead` signal is emitted. A failure to read the value triggers the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicReadError`. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic` function attempts to write a new value to the given characteristic. If the write attempt is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten` signal is emitted. A failure to write triggers the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError`. Reading and writing of descriptors follows the same pattern.

Every attempt is made to read or write the value of a descriptor or characteristic on the hardware. This means that meta information such as :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.properties` is generally ignored when reading and writing. As an example, it is possible to call :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic` despite the characteristic being read-only based on its meta data description. The resulting write request is forwarded to the connected device and it is up to the device to respond to the potentially invalid request. In this case the result is the emission of the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError` in response to the returned device error. This behavior simplifies interaction with devices which report wrong meta information. If it was not possible to forward the request to the remote device the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.OperationError` is set. A potential reason could be that the to-be-written characteristic object does not even belong the current service. In summary, the two types of errors permit a quick distinction of local and remote error cases.

All requests are serialised based on First-In First-Out principle. For example, issuing a second write request, before the previous write request has finished, is delayed until the first write request has finished.

**Note:** Currently, it is not possible to send signed write or reliable write requests.

.. _qlowenergyservice-notifications:

In some cases the peripheral generates value updates which the central is interested in receiving. In order for a characteristic to support such notifications it must have the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Notify` or :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Indicate` property and a descriptor of type :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid.DescriptorType.ClientCharacteristicConfiguration`. Provided those conditions are fulfilled notifications can be enabled as shown in the following code segment:

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-doc-snippets-doc_src_qtbluetooth.py
    :lines: 204-226

The example shows a battery level characteristic which updates the central on every value change. The notifications are provided via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicChanged` signal. More details about this mechanism are provided by the `Bluetooth Specification <https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorViewer.aspx?u=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml>`_.

.. _qlowenergyservice-service-data-sharing:

Service Data Sharing
--------------------

Each :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` instance shares its internal states and information with other :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` instance of the same service. If one instance initiates the discovery of the service details, all remaining instances automatically follow. Therefore the following snippet always works:

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-doc-snippets-doc_src_qtbluetooth.py
    :lines: 169-183

Other operations such as calls to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readDescriptor`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeDescriptor` or the invalidation of the service due to the related `QLowEnergyController <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycontroller>`_ disconnecting from the device are shared the same way.

.. seealso:: `QLowEnergyController <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycontroller>`_, `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_, `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_.
