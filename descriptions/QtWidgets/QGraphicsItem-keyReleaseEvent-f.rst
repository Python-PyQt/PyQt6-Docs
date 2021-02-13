.. sip:method-description::
    :status: todo
    :pysig: ce3d9b4daef6744486b5f293221f93ba
    :realsig: (QKeyEvent*)
    :digest: 6d0d7b95b16d84b8edbe77081b8401ad

This event handler, for event *event*, can be reimplemented to receive key release events for this item. The default implementation ignores the event. If you reimplement this handler, the event will by default be accepted.

Note that key events are only received for items that set the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsFocusable` flag, and that have keyboard input focus.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.keyPressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocusItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
