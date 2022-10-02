.. sip:signal-description::
    :status: todo
    :pysig: e8a10dcde1fc9bdc27f270edd3719591
    :realsig: (const QLowEnergyCharacteristic&,const QByteArray&)
    :digest: 15da3867688ccf977e4ec49a7bf8795b

This signal is emitted when the value of *characteristic* is successfully changed to *newValue*. The change must have been triggered by calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic`. If the write operation is not successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.errorOccurred` signal is emitted using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError` flag.

The reception of the written signal can be considered as a sign that the target device received the to-be-written value and reports back the status of write request.

**Note:** If :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic` is called using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteWithoutResponse` mode, this signal and the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.errorOccurred` are never emitted.

**Note:** This signal is only emitted for Central Role related use cases.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic`.
