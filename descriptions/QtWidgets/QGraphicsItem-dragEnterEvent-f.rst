.. sip:method-description::
    :status: todo
    :pysig: 33e861446b7ae472c03779419970a4fa
    :realsig: (QGraphicsSceneDragDropEvent*)
    :digest: 9d256ad5c6df8a28ede43cce7184099b

This event handler, for event *event*, can be reimplemented to receive drag enter events for this item. Drag enter events are generated as the cursor enters the item's area.

By accepting the event (i.e., by calling :sip:ref:`~PyQt6.QtCore.QEvent.accept`), the item will accept drop events, in addition to receiving drag move and drag leave. Otherwise, the event will be ignored and propagate to the item beneath. If the event is accepted, the item will receive a drag move event before control goes back to the event loop.

A common implementation of  accepts or ignores *event* depending on the associated mime data in *event*. Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 208-217

Items do not receive drag and drop events by default; to enable this feature, call ``setAcceptDrops(true)``.

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dropEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragLeaveEvent`.
