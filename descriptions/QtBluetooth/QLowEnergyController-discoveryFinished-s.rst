.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 395c324d3721d28b1f86c9ea1e761359

This signal is emitted when the running service discovery finishes. The signal is not emitted if the discovery process finishes with an error.

This signal can only be emitted if the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.CentralRole`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.discoverServices`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.error`.
