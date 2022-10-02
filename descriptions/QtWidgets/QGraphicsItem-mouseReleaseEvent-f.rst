.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: 6f745d33b2cd636a8ce31f14671c1162

This event handler, for event *event*, can be reimplemented to receive mouse release events for this item.

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* has no effect.

The default implementation handles basic item interaction, such as selection and moving. If you want to keep the base implementation when reimplementing this function, call QGraphicsItem::mouseReleaseEvent() in your reimplementation.

Please note that :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent` decides which graphics item it is that receives mouse events. See the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent` description for details.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
