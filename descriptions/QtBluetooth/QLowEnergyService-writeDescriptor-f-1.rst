.. sip:method-description::
    :status: todo
    :pysig: f058a73e371eb1b77c72d5ef23241b96
    :realsig: (const QLowEnergyDescriptor&, const QByteArray&)
    :digest: 252bbc3ed2fde45463958c4228faec0b

Writes *newValue* as value for *descriptor*. The exact semantics depend on the role that the associated controller object is in.

**Central role**

A call to this function results in a write request to the remote device. If the operation is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.descriptorWritten` signal is emitted; otherwise the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.DescriptorWriteError` is emitted.

All descriptor and characteristic requests towards the same remote device are serialised. A queue is employed when issuing multiple write requests at the same time. The queue does not eliminate duplicated write requests for the same descriptor. For example, if the same descriptor is set to the value A and immediately afterwards to B, the two write request are executed in the given order.

A descriptor can only be written if this service is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state, belongs to the service. If one of these conditions is not true the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.OperationError` is set.

**Peripheral Role**

The value is written to the local service database. If the contents of *newValue* are not valid for *descriptor*, the behavior is unspecified.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.descriptorWritten`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readDescriptor`.
