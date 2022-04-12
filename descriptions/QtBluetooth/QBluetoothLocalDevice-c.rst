.. sip:class-description::
    :status: todo
    :brief: Enables access to the local Bluetooth device
    :digest: 26b913a12d0aae3e43f6e7098d39711b

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` class enables access to the local Bluetooth device.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` provides functions for getting and setting the state of local Bluetooth devices.

On iOS, this class cannot be used because the platform does not expose any data or API which may provide information on the local Bluetooth device.

On Windows the class is not fully implemented. It does not support tracking of the connected/disconnected devices. Therefore, the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.connectedDevices` method will always return an empty list, and the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.deviceConnected` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.deviceDisconnected` signals will never be emitted.
