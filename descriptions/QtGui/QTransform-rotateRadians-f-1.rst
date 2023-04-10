.. sip:method-description::
    :status: todo
    :pysig: aea7fdd9776ffd02e4bec431446a6029
    :realsig: (qreal,Qt::Axis,qreal)
    :digest: 62ee785b1cb8b1a29c0345206dd6a5da

Rotates the coordinate system counterclockwise by the given angle *a* about the specified *axis* at distance *distanceToPlane* from the screen and returns a reference to the matrix.

Note that if you apply a :sip:ref:`~PyQt6.QtGui.QTransform` to a point defined in widget coordinates, the direction of the rotation will be clockwise because the y-axis points downwards.

The angle is specified in radians. If *distanceToPlane* is zero, it will be ignored. This is suitable for implementing orthographic projections where the z coordinate should be dropped rather than projected.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTransform.setMatrix`.
