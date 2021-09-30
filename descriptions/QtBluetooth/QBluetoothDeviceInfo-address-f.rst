.. sip:method-description::
    :status: todo
    :pysig: 15bb6dd4c08c32ed8272c0814d30eefa
    :realsig: () const
    :digest: 588d7af989294eac80529092281edc0f

Returns the address of the device.

**Note:** On iOS and macOS this address is invalid. Instead :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.deviceUuid` should be used. Those two platforms do not expose Bluetooth addresses for found Bluetooth devices and utilize unique device identifiers.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.deviceUuid`.
