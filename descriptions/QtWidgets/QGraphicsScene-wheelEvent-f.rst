.. sip:method-description::
    :status: todo
    :pysig: 3bf5e40c5fdb6cc7ae120183969e4630
    :realsig: (QGraphicsSceneWheelEvent*)
    :digest: 2c50308b3b9916c8bdaa000ae1e3035f

This event handler, for event *wheelEvent*, can be reimplemented in a subclass to receive mouse wheel events for the scene.

By default, the event is delivered to the topmost visible item under the cursor. If ignored, the event propagates to the item beneath, and again until the event is accepted, or it reaches the scene. If no items accept the event, it is ignored.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.wheelEvent`.
