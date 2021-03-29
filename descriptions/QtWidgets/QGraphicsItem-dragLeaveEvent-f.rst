.. sip:method-description::
    :status: todo
    :pysig: 33e861446b7ae472c03779419970a4fa
    :realsig: (QGraphicsSceneDragDropEvent*)
    :digest: 8979af79c1ed62514a7dc8304d0cdfbd

This event handler, for event *event*, can be reimplemented to receive drag leave events for this item. Drag leave events are generated as the cursor leaves the item's area. Most often you will not need to reimplement this function, but it can be useful for resetting state in your item (e.g., highlighting).

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* has no effect.

Items do not receive drag and drop events by default; to enable this feature, call ``setAcceptDrops(true)``.

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dropEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragMoveEvent`.
