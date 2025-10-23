.. sip:method-description::
    :status: todo
    :pysig: a534763fda2a6447a4ed990c693f21f2
    :realsig: (qreal,Qt::Axis)
    :digest: d2113dc526fba2c2134a4e7fe989ae7d

Rotates the coordinate system counterclockwise by the given angle *a* about the specified *axis* at distance 1024.0 from the screen and returns a reference to the matrix.

Note that if you apply a :sip:ref:`~PyQt6.QtGui.QTransform` to a point defined in widget coordinates, the direction of the rotation will be clockwise because the y-axis points downwards.

The angle is specified in degrees.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTransform.setMatrix`.
