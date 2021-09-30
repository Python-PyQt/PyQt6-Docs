.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: a94889a0147d65d8ea7fbf732625a5f2

If a characteristic is written using this mode, the peripheral shall send a write confirmation. If the operation is successful, the confirmation is emitted via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten` signal. Otherwise the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError` is emitted. A characteristic must have set the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Write` property to support this write mode.
