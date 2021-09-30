.. sip:class-description::
    :status: todo
    :brief: Represents the data to be broadcast during Bluetooth Low Energy advertising
    :digest: adee100739f4d82e5a7c57bfbf87da77

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData` class represents the data to be broadcast during Bluetooth Low Energy advertising.

This data can include the device name, GATT services offered by the device, and so on. The data set via this class will be used when advertising is started by calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising`. Objects of this class can represent an Advertising Data packet or a Scan Response packet.

**Note:** The actual data packets sent over the advertising channel cannot contain more than 31 bytes. If the variable-length data set via this class exceeds that limit, it will be left out of the packet or truncated, depending on the type.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingParameters`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising`.
