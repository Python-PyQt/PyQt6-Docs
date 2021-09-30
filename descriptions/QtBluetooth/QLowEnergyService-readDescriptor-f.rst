.. sip:method-description::
    :status: todo
    :pysig: 6e862321188e0284d08325e12acf151e
    :realsig: (const QLowEnergyDescriptor&)
    :digest: 400826e15fea9cf99a15f07159045903

Reads the value of *descriptor*. If the operation is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.descriptorRead` signal is emitted; otherwise the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.DescriptorReadError` is set.

All descriptor and characteristic requests towards the same remote device are serialised. A queue is employed when issuing multiple requests at the same time. The queue does not eliminate duplicated read requests for the same descriptor.

A descriptor can only be read if the service is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state and the descriptor belongs to the service. If one of these conditions is not true the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.OperationError` is set.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.descriptorRead`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeDescriptor`.
