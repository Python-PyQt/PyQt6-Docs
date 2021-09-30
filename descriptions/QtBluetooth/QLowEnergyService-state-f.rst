.. sip:method-description::
    :status: todo
    :pysig: df13f3f83eb025c75c2f60d12b039bb2
    :realsig: () const
    :digest: 810ae35a9b0c04302d69eecb1be03dcf

Returns the current state of the service.

If the device's service was instantiated for the first time, the object's state is :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveryRequired`. The state of all service objects which point to the same service on the peripheral device are always equal. This is caused by the shared nature of the internal object data. Therefore any service object instance created after the first one has a state equal to already existing instances.

A service becomes invalid if the `QLowEnergyController <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycontroller>`_ disconnects from the remote device. An invalid service retains its internal state at the time of the disconnect event. This implies that once the service details are discovered they can even be retrieved from an invalid service. This permits scenarios where the device connection is established, the service details are retrieved and the device immediately disconnected to permit the next device to connect to the peripheral device.

However, under normal circumstances the connection should remain to avoid repeated discovery of services and their details. The discovery may take a while and the client can subscribe to ongoing change notifications.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.stateChanged`.
