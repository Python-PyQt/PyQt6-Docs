.. sip:signal-description::
    :status: todo
    :pysig: d95e803c4d97606ac556c139127b5331
    :realsig: (const QLowEnergyDescriptor&,const QByteArray&)
    :digest: b89e4b68448775283d06c7a47e83bca7

This signal is emitted when the read request for *descriptor* successfully returned its *value*. The signal might be triggered by calling descriptorRead(). If the read operation is not successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.errorOccurred` signal is emitted using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.DescriptorReadError` flag.

**Note:** This signal is only emitted for Central Role related use cases.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readDescriptor`.
