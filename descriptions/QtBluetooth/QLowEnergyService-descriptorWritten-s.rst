.. sip:signal-description::
    :status: todo
    :pysig: d95e803c4d97606ac556c139127b5331
    :realsig: (const QLowEnergyDescriptor&,const QByteArray&)
    :digest: 78f0339c69d796c2417ccf0f56b05701

This signal is emitted when the value of *descriptor* is successfully changed to *newValue*. If the associated controller object is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.CentralRole` role, the change must have been caused by calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeDescriptor`. Otherwise, the signal is the result of a write request or command from a GATT client to the respective descriptor.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeDescriptor`.
