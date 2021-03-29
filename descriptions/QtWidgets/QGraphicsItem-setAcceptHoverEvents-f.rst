.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 9afcca32352d67962e2a76e0cddf1709

If *enabled* is true, this item will accept hover events; otherwise, it will ignore them. By default, items do not accept hover events.

Hover events are delivered when there is no current mouse grabber item. They are sent when the mouse cursor enters an item, when it moves around inside the item, and when the cursor leaves an item. Hover events are commonly used to highlight an item when it's entered, and for tracking the mouse cursor as it hovers over the item (equivalent to QWidget::mouseTracking).

Parent items receive hover enter events before their children, and leave events after their children. The parent does not receive a hover leave event if the cursor enters a child, though; the parent stays "hovered" until the cursor leaves its area, including its children's areas.

If a parent item handles child events, it will receive hover move, drag move, and drop events as the cursor passes through its children, but it does not receive hover enter and hover leave, nor drag enter and drag leave events on behalf of its children.

A `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ with window decorations will accept hover events regardless of the value of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptHoverEvents`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptHoverEvents`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverLeaveEvent`.
