.. sip:method-description::
    :status: todo
    :pysig: b6da2bfae229ab0448ace11dffdc01bb
    :realsig: (const QPointF&,const QPointF&)
    :digest: 28a02cc5de84de79ea425441785e734c

Adds a quadratic Bezier curve between the current position and the given *endPoint* with the control point specified by *c*.

After the curve is added, the current point is updated to be at the end point of the curve.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.cubicTo`, Composing a QPainterPath.
