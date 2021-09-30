.. sip:signal-description::
    :status: todo
    :pysig: e8a10dcde1fc9bdc27f270edd3719591
    :realsig: (const QLowEnergyCharacteristic&,const QByteArray&)
    :digest: 12613d238ebc4aefee60b478c059c30b

This signal is emitted when the read request for *characteristic* successfully returned its *value*. The signal might be triggered by calling characteristicRead(). If the read operation is not successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.error` signal is emitted using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicReadError` flag.

**Note:** This signal is only emitted for Central Role related use cases.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic`.
