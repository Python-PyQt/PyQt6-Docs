.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 016bd033e5a07fc6a6909a8336a61a8c

If a characteristic is written using this mode, the remote peripheral shall not send a write confirmation. The operation's success cannot be determined and the payload must not be longer than 8 bytes. A bond must exist between the two devices and the link must not be encrypted. A characteristic must have set the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteSigned` property to support this write mode. This value was introduced in Qt 5.7 and is currently only supported on Android and on Linux with BlueZ 5 and a kernel version 3.7 or newer.
