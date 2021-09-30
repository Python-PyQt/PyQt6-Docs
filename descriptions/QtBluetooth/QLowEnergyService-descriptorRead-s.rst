.. sip:signal-description::
    :status: todo
    :pysig: d95e803c4d97606ac556c139127b5331
    :realsig: (const QLowEnergyDescriptor&,const QByteArray&)
    :digest: e7af7c73c30dcf4bce9dfe7f97a6e11d

This signal is emitted when the read request for *descriptor* successfully returned its *value*. The signal might be triggered by calling descriptorRead(). If the read operation is not successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.error` signal is emitted using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.DescriptorReadError` flag.

**Note:** This signal is only emitted for Central Role related use cases.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readDescriptor`.
