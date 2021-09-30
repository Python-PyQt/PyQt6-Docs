.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 8ac8738fe3f74ced1e3b63042a4a2651

Returns the maximum connection interval in milliseconds. The default is 4000.

**Note:** If this object was emitted via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectionUpdated`, then this value is the same as :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.minimumInterval` and refers to the actual connection interval.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.setIntervalRange`.
