.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: ecad67c454df925820bba29bb1a6ca91

This event handler, for event *event*, can be reimplemented to receive mouse press events for this item. Mouse press events are only delivered to items that accept the mouse button that is pressed. By default, an item accepts all mouse buttons, but you can change this by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptedMouseButtons`.

The mouse press event decides which item should become the mouse grabber (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mouseGrabberItem`). If you do not reimplement this function, the press event will propagate to any topmost item beneath this item, and no other mouse events will be delivered to this item.

If you do reimplement this function, *event* will by default be accepted (see :sip:ref:`~PyQt6.QtCore.QEvent.accept`), and this item is then the mouse grabber. This allows the item to receive future move, release and double-click events. If you call :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on *event*, this item will lose the mouse grab, and *event* will propagate to any topmost item beneath. No further mouse events will be delivered to this item unless a new mouse press event is received.

The default implementation handles basic item interaction, such as selection and moving. If you want to keep the base implementation when reimplementing this function, call QGraphicsItem::mousePressEvent() in your reimplementation.

The event is :sip:ref:`~PyQt6.QtCore.QEvent.ignore`\ d for items that are neither :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable` nor :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
