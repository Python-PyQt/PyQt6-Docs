.. sip:method-description::
    :status: todo
    :pysig: 568b014a366a71095f4f9661cf095121
    :realsig: (qreal,qreal,qreal,qreal,qreal)
    :digest: 79b5756cde2d5542f5c385fb6048d897

Constructs a simple radial gradient with the given center (\ *cx*, *cy*), *radius* and focal point (\ *fx*, *fy*).

**Note:** If the given focal point is outside the circle defined by the center (\ *cx*, *cy*) and the *radius* it will be re-adjusted to the intersection between the line from the center to the focal point and the circle.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGradient.setColorAt`, :sip:ref:`~PyQt6.QtGui.QGradient.setStops`.
