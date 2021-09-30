.. sip:signal-description::
    :status: todo
    :pysig: 6763f06f87fc85e4e0e37b1c647e6327
    :realsig: (const QLowEnergyConnectionParameters&)
    :digest: b6b17e59dae44de777dfa75ebb8a21b3

This signal is emitted when the connection parameters change. This can happen as a result of calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.requestConnectionUpdate` or due to other reasons, for instance because the other side of the connection requested new parameters. The new values can be retrieved from *newParameters*.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.requestConnectionUpdate`.
