.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: 306633497fd6ebdd7ac700bcf64e0dff

This event handler, for event *mouseEvent*, can be reimplemented in a subclass to receive mouse release events for the scene.

The default implementation depends on the mouse grabber state. If there is no mouse grabber, the event is ignored. Otherwise, if there is a mouse grabber item, the event is sent to the mouse grabber. If this mouse release represents the last pressed button on the mouse, the mouse grabber item then loses the mouse grab.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptedMouseButtons`.
