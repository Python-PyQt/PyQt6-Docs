.. sip:method-description::
    :status: todo
    :pysig: a534763fda2a6447a4ed990c693f21f2
    :realsig: (qreal,Qt::Axis)
    :digest: b4c1882fbf993ce6854ac21af61b87f6

Rotates the coordinate system counterclockwise by the given *angle* about the specified *axis* and returns a reference to the matrix.

Note that if you apply a :sip:ref:`~PyQt6.QtGui.QTransform` to a point defined in widget coordinates, the direction of the rotation will be clockwise because the y-axis points downwards.

The angle is specified in radians.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTransform.setMatrix`.
