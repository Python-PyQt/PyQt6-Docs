.. sip:method-description::
    :status: todo
    :pysig: 541c2c6a2fd633bf559421eae8af88d7
    :realsig: (QVector3D,QVector3D,QVector3D) const
    :digest: ba4870d80ac441c26ed81496b9aff5da

Returns the distance from this vertex to a plane defined by the vertices *plane1*, *plane2* and *plane3*.

The return value will be negative if the vertex is below the plane, or zero if it is on the plane.

The two vectors that define the plane are *plane2* - *plane1* and *plane3* - *plane1*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.normal`, :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToLine`.
