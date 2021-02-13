.. sip:method-description::
    :status: todo
    :pysig: 33e861446b7ae472c03779419970a4fa
    :realsig: (QGraphicsSceneDragDropEvent*)
    :digest: c0c362f04631e7925b434f151ce08dd9

This event handler, for event *event*, can be reimplemented to receive drop events for this item. Items can only receive drop events if the last drag move event was accepted.

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* has no effect.

Items do not receive drag and drop events by default; to enable this feature, call ``setAcceptDrops(true)``.

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragLeaveEvent`.
