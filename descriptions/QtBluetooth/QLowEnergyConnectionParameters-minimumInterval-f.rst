.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 247c497609c2daba4bcb0ed3964d4bb7

Returns the minimum connection interval in milliseconds. The default is 7.5.

**Note:** If this object was emitted via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectionUpdated`, then this value is the same as :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.maximumInterval` and refers to the actual connection interval.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.setIntervalRange`.
