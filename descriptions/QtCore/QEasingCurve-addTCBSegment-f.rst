.. sip:method-description::
    :status: todo
    :pysig: daaf59fe7fd29ac41a8f7a58c624e32f
    :realsig: (const QPointF&,qreal,qreal,qreal)
    :digest: 0f51b56ca53c6fcbfd375991bab0524f

Adds a segment of a TCB bezier spline to define a custom easing curve. It is only applicable if :sip:ref:`~PyQt6.QtCore.QEasingCurve.type` is :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.TCBSpline`. The spline has to start explitly at (0.0, 0.0) and has to end at (1.0, 1.0) to be a valid easing curve. The tension *t* changes the length of the tangent vector. The continuity *c* changes the sharpness in change between the tangents. The bias *b* changes the direction of the tangent vector. *nextPoint* is the sample position. All three parameters are valid between -1 and 1 and define the tangent of the control point. If all three parameters are 0 the resulting spline is a Catmull-Rom spline. The begin and endpoint always have a bias of -1 and 1, since the outer tangent is not defined.
