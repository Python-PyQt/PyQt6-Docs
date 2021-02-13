.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 9d04acea0c74160a764cc660cf8bb558

If *visible* is true, the item is made visible. Otherwise, the item is made invisible. Invisible items are not painted, nor do they receive any events. In particular, mouse events pass right through invisible items, and are delivered to any item that may be behind. Invisible items are also unselectable, they cannot take input focus, and are not detected by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`'s item location functions.

If an item becomes invisible while grabbing the mouse, (i.e., while it is receiving mouse events,) it will automatically lose the mouse grab, and the grab is not regained by making the item visible again; it must receive a new mouse press to regain the mouse grab.

Similarly, an invisible item cannot have focus, so if the item has focus when it becomes invisible, it will lose focus, and the focus is not regained by simply making the item visible again.

If you hide a parent item, all its children will also be hidden. If you show a parent item, all children will be shown, unless they have been explicitly hidden (i.e., if you call (false) on a child, it will not be reshown even if its parent is hidden, and then shown again).

Items are visible by default; it is unnecessary to call  on a new item.

**Note:** An item with opacity set to 0 will still be considered visible, although it will be treated like an invisible item: mouse events will pass through it, it will not be included in the items returned by :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, and so on. However, the item will retain the focus.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.show`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hide`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setOpacity`.
