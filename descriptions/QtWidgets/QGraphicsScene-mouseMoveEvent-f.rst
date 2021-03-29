.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: c1f3e24b1a8c810546d7a3c34a42c94f

This event handler, for event *mouseEvent*, can be reimplemented in a subclass to receive mouse move events for the scene.

The default implementation depends on the mouse grabber state. If there is a mouse grabber item, the event is sent to the mouse grabber. If there are any items that accept hover events at the current position, the event is translated into a hover event and accepted; otherwise it's ignored.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptedMouseButtons`.
