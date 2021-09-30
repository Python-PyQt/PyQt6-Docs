.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cbc58acd0773f5908fea17dc2658a687

Stops advertising, if this object is currently in the advertising state.

The controller has to be in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole` for this function to work. It does not invalidate services which have previously been added via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.addService`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising`.
