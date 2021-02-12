.. sip:method-description::
    :status: todo
    :pysig: 32603454d4f10fa678787c4571fc43de
    :realsig: (const QPointF&,const QPointF&,const QPointF&)
    :digest: 1323cb096ff8e9881a2568c56caacdf6

Adds a segment of a cubic bezier spline to define a custom easing curve. It is only applicable if :sip:ref:`~PyQt6.QtCore.QEasingCurve.type` is :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.BezierSpline`. Note that the spline implicitly starts at (0.0, 0.0) and has to end at (1.0, 1.0) to be a valid easing curve. *c1* and *c2* are the control points used for drawing the curve. *endPoint* is the endpoint of the curve.
