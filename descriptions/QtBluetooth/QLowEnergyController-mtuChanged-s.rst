.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 00b92e2da91a8466319a51bb9ea5af5c

This signal is emitted as a result of a successful MTU change. *mtu* represents the new value.

**Note:** If the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole`, the MTU value is negotiated for each client/central device individually. Therefore this signal can be emitted several times in a row for one or several devices.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.mtu`.
