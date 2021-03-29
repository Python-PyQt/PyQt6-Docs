.. sip:method-description::
    :status: todo
    :pysig: d24f41455674f08ba5aa95261b9ba83c
    :realsig: (const QRectF&)
    :digest: a78a93fa2bb6dcdaeccd46e6288059e7

Schedules a redraw of the area covered by *rect* in this item. You can call this function whenever your item needs to be redrawn, such as if it changes appearance or size.

This function does not cause an immediate paint; instead it schedules a paint request that is processed by :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` after control reaches the event loop. The item will only be redrawn if it is visible in any associated view.

As a side effect of the item being repainted, other items that overlap the area *rect* may also be repainted.

If the item is invisible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``false``), this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`.
