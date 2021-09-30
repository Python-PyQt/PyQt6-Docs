.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: d37ec1c6fd961af35f0027d45c3649f4

Sets the link supervision timeout to *timeout* milliseconds. There are several constraints on this value: It must be in the range [100,32000] and it must be larger than (1 + :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.latency`) \* 2 \* :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.maximumInterval`.

On Android, this timeout is not adjustable and therefore ignored.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.supervisionTimeout`.
