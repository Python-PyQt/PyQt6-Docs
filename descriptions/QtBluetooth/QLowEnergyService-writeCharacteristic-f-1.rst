.. sip:method-description::
    :status: todo
    :pysig: eaba6e055e096d9b0c33cdac4955c5b4
    :realsig: (const QLowEnergyCharacteristic&, const QByteArray&, QLowEnergyService::WriteMode)
    :digest: 3c3229023dad2ad890fe8c4cfd50bd61

Writes *newValue* as value for the *characteristic*. The exact semantics depend on the role that the associated controller object is in.

**Central role**

The call results in a write request or command to a remote peripheral. If the operation is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten` signal is emitted; otherwise the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError` is set. Calling this function does not trigger the a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicChanged` signal unless the peripheral itself changes the value again after the current write request.

The *mode* parameter determines whether the remote device should send a write confirmation. The to-be-written *characteristic* must support the relevant write mode. The characteristic's supported write modes are indicated by its :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Write` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteNoResponse` properties.

All descriptor and characteristic write requests towards the same remote device are serialised. A queue is employed when issuing multiple write requests at the same time. The queue does not eliminate duplicated write requests for the same characteristic. For example, if the same descriptor is set to the value A and immediately afterwards to B, the two write request are executed in the given order.

**Note:** Currently, it is not possible to use signed or reliable writes as defined by the Bluetooth specification.

A characteristic can only be written if this service is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state and belongs to the service. If one of these conditions is not true the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.OperationError` is set.

**Note:** Calling this function despite :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.properties` reporting a non-writable property always attempts to write to the hardware. Similarly, a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteWithoutResponse` is sent to the hardware too although the characteristic may only support :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteWithResponse`. If the hardware returns with an error the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError` is set.

**Peripheral role**

The call results in the value of the characteristic getting updated in the local database.

If a client is currently connected and it has enabled notifications or indications for the characteristic, the respective information will be sent. If a device has enabled notifications or indications for the characteristic and that device is currently not connected, but a bond exists between it and the local device, then the notification or indication will be sent on the next reconnection.

If there is a constraint on the length of the characteristic value and *newValue* does not adhere to that constraint, the behavior is unspecified.

**Note:** The *mode* argument is ignored in peripheral mode.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic`.
