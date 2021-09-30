.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: aa933c33012109ae6c25797a97a511cf

This signal is emitted when the controller successfully connects to the remote Low Energy device (if the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.CentralRole`) or if a remote Low Energy device connected to the controller (if the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole`). On iOS and OS X this signal is not reliable if the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole` - the controller only guesses that some central connected to our peripheral as soon as this central tries to write/read a characteristic/descriptor.
