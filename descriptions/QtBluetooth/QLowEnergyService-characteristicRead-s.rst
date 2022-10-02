.. sip:signal-description::
    :status: todo
    :pysig: e8a10dcde1fc9bdc27f270edd3719591
    :realsig: (const QLowEnergyCharacteristic&,const QByteArray&)
    :digest: 099c2fd02624c4768477830fa5081852

This signal is emitted when the read request for *characteristic* successfully returned its *value*. The signal might be triggered by calling characteristicRead(). If the read operation is not successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.errorOccurred` signal is emitted using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicReadError` flag.

**Note:** This signal is only emitted for Central Role related use cases.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic`.
