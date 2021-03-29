.. sip:method-description::
    :status: todo
    :pysig: 260972f99a860cc803ca03f81f7cd641
    :realsig: (QGraphicsSceneMoveEvent*)
    :digest: 8638558768bf31f5de0cbe44d065a7fc

This event handler, for :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneMove` events, is delivered after the widget has moved (e.g., its local position has changed).

This event is only delivered when the item is moved locally. Calling setTransform() or moving any of the item's ancestors does not affect the item's local position.

You can reimplement this event handler to detect when your widget has moved. Calling :sip:ref:`~PyQt6.QtCore.QEvent.accept` or :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on *event* has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged`.
