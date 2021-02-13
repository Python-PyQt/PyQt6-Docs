.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 68de905dfe298e4c6df0cf8d83e0a051

Returns the tangential pressure for the device. This is typically given by a finger wheel on an airbrush tool. The range is from -1.0 to 1.0. 0.0 indicates a neutral position. Current airbrushes can only move in the positive direction from the neutrual position. If the device does not support tangential pressure, this value is always 0.0.

**Note:** The value is stored as a single-precision float.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTabletEvent.pressure`.
