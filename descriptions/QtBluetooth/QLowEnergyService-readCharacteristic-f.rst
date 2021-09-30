.. sip:method-description::
    :status: todo
    :pysig: 16271410e58dae265e710062fa68602e
    :realsig: (const QLowEnergyCharacteristic&)
    :digest: 655e53737a9730ca2b80995b270ea248

Reads the value of *characteristic*. If the operation is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicRead` signal is emitted; otherwise the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicReadError` is set. In general, a *characteristic* is readable, if its :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Read` property is set.

All descriptor and characteristic requests towards the same remote device are serialised. A queue is employed when issuing multiple requests at the same time. The queue does not eliminate duplicated read requests for the same characteristic.

A characteristic can only be read if the service is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state and belongs to the service. If one of these conditions is not true the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.OperationError` is set.

**Note:** Calling this function despite :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.properties` reporting a non-readable property always attempts to read the characteristic's value on the hardware. If the hardware returns with an error the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicReadError` is set.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicRead`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic`.
