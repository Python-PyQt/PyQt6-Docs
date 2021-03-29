.. sip:method-description::
    :status: todo
    :pysig: b6da2bfae229ab0448ace11dffdc01bb
    :realsig: (const QPointF&) const
    :digest: 4b23df4cf73be8e4aff26b14fe712072

Returns the scene-local coordinates if the *gesturePoint* is inside a graphics view.

This functional might be useful when the gesture event is delivered to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject` to translate a point in screen coordinates to scene-local coordinates.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPointF.isNull`.
