.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 54bc03b9a9ad050ea24247f73f784cfb

If a characteristic is written using this mode, the remote peripheral shall not send a write confirmation. The operation's success cannot be determined and the payload must not be longer than 20 bytes. A characteristic must have set the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteNoResponse` property to support this write mode. Its adavantage is a quicker write operation as it may happen in between other device interactions.
