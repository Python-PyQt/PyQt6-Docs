.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: ef856786d95bec1559dba724b100aafa

Returns the angle between the device (a pen, for example) and the perpendicular in the direction of the x axis. Positive values are towards the tablet's physical right. The angle is in the range -60 to +60 degrees.

.. image:: ../../../images/qtabletevent-tilt.png

**Note:** The value is stored as a single-precision float.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTabletEvent.yTilt`.
