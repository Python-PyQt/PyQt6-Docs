.. sip:signal-description::
    :status: todo
    :pysig: 2e954e7da9b1ceaf30a250b5934505e1
    :realsig: (const QLowEnergyCharacteristic&, const QByteArray&)
    :digest: f76cdc3a1f2a9116f87ddc0315c04705

If the associated controller object is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.CentralRole` role, this signal is emitted when the value of *characteristic* is changed by an event on the peripheral/device side. In that case, the signal emission implies that change notifications must have been activated via the characteristic's :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid.DescriptorType.ClientCharacteristicConfiguration` descriptor prior to the change event on the peripheral. More details on how this might be done can be found further above.

If the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole` role, that is, the service object was created via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.addService`, the signal is emitted when a GATT client has written the value of the characteristic using a write request or command.

The *newValue* parameter contains the updated value of the *characteristic*.
