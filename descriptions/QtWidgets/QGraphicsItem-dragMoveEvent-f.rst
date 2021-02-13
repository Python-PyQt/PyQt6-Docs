.. sip:method-description::
    :status: todo
    :pysig: 33e861446b7ae472c03779419970a4fa
    :realsig: (QGraphicsSceneDragDropEvent*)
    :digest: 779a5ac5f3c0b482f41807b982a4241b

This event handler, for event *event*, can be reimplemented to receive drag move events for this item. Drag move events are generated as the cursor moves around inside the item's area. Most often you will not need to reimplement this function; it is used to indicate that only parts of the item can accept drops.

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* toggles whether or not the item will accept drops at the position from the event. By default, *event* is accepted, indicating that the item allows drops at the specified position.

Items do not receive drag and drop events by default; to enable this feature, call ``setAcceptDrops(true)``.

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dropEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragLeaveEvent`.
