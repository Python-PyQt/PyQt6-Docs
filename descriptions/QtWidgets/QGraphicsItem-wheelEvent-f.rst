.. sip:method-description::
    :status: todo
    :pysig: 3bf5e40c5fdb6cc7ae120183969e4630
    :realsig: (QGraphicsSceneWheelEvent*)
    :digest: bc5e28e674cff908aa0e368f38d28d2e

This event handler, for event *event*, can be reimplemented to receive wheel events for this item. If you reimplement this function, *event* will be accepted by default.

If you ignore the event, (i.e., by calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore`,) it will propagate to any item beneath this item. If no items accept the event, it will be ignored by the scene, and propagate to the view (e.g., the view's vertical scroll bar).

The default implementation ignores the event.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
