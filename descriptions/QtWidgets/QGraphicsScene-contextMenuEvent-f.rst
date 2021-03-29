.. sip:method-description::
    :status: todo
    :pysig: 6702e72b0e187fd9655ed4b8376208c5
    :realsig: (QGraphicsSceneContextMenuEvent*)
    :digest: 84cd66a3a6ea80c4d686648781f0d1be

This event handler, for event *contextMenuEvent*, can be reimplemented in a subclass to receive context menu events. The default implementation forwards the event to the topmost visible item that accepts context menu events at the position of the event. If no items accept context menu events at this position, the event is ignored.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contextMenuEvent`.
