.. sip:method-description::
    :status: todo
    :pysig: 15bb6dd4c08c32ed8272c0814d30eefa
    :realsig: () const
    :digest: 440a7d55711f8509413741d8e9d12c44

Returns the address of the remote Bluetooth Low Energy device.

For a controller in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.CentralRole`, this value will always be the one passed in when the controller object was created. For a controller in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole`, this value is the address of the currently connected client device. In particular, this address will be invalid if the controller is not currently in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.ControllerState.ConnectedState`.
