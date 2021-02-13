.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: c4fafec5f9fcf174cc3252394e3ca1f4

This event handler, for event *event*, can be reimplemented to receive mouse doubleclick events for this item.

When doubleclicking an item, the item will first receive a mouse press event, followed by a release event (i.e., a click), then a doubleclick event, and finally a release event.

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* has no effect.

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`. If you want to keep the base implementation when reimplementing this function, call  in your reimplementation.

Note that an item will not receive double click events if it is neither :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsSelectable` nor :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsMovable` (single mouse clicks are ignored in this case, and that stops the generation of double clicks).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
