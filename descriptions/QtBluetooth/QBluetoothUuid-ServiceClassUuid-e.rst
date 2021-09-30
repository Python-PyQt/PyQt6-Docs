.. sip:enum-description::
    :status: todo
    :digest: 6ced9777272d0ad50169aab7429286cc

This enum is a convienience type for Bluetooth service class and profile UUIDs. Values of this type will be implicitly converted into a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid` when necessary. Some UUIDs refer to service class ids, others to profile ids and some can be used as both. In general, profile UUIDs shall only be used in a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.BluetoothProfileDescriptorList` attribute and service class UUIDs shall only be used in a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.ServiceClassIds` attribute. If the UUID is marked as profile and service class UUID it can be used as a value for either of the above service attributes. Such a dual use has historical reasons but is no longer permissible for newer UUIDs.

The list below explicitly states as what type each UUID shall be used. Bluetooth Low Energy related values starting with 0x18 were introduced by Qt 5.4
