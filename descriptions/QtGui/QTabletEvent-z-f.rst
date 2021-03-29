.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 478c8fcdc64c880e2b7ab6aae32deb9c

Returns the z position of the device. Typically this is represented by a wheel on a 4D Mouse. If the device does not support a Z-axis, this value is always zero. This is **not** the same as pressure.

**Note:** The value is stored as a single-precision float.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTabletEvent.pressure`.
