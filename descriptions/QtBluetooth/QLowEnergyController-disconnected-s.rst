.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a396e362d489f4a66483f36784e391ef

This signal is emitted when the controller disconnects from the remote Low Energy device or vice versa. On iOS and macOS this signal is unreliable if the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole`. On Android the signal is emitted when the last connected device is disconnected.
