.. sip:method-description::
    :status: todo
    :pysig: d44a710c000db38a04264ffb04a16396
    :realsig: (QVector3D,QVector3D) const
    :digest: 168bc33ee078f94a00e4463a1cb7be61

Returns the distance from this vertex to a plane defined by the vertex *plane* and a *normal* unit vector. The *normal* parameter is assumed to have been normalized to a unit vector.

The return value will be negative if the vertex is below the plane, or zero if it is on the plane.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.normal`, :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToLine`.
