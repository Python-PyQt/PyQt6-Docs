.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: b329548fa03033a07000cd191fbe83a9

This event handler, for event *mouseEvent*, can be reimplemented in a subclass to receive mouse press events for the scene.

The default implementation depends on the state of the scene. If there is a mouse grabber item, then the event is sent to the mouse grabber. Otherwise, it is forwarded to the topmost visible item that accepts mouse events at the scene position from the event, and that item promptly becomes the mouse grabber item.

If there is no item at the given position on the scene, the selection area is reset, any focus item loses its input focus, and the event is then ignored.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptedMouseButtons`.
