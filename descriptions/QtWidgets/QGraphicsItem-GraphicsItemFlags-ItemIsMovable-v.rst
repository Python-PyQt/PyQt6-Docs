.. sip:enum-member-description::
    :status: todo
    :value: 0x1
    :realname: QGraphicsItem::GraphicsItemFlag::ItemIsMovable
    :digest: 27cd2dca1d5ac3c99348b8b43bf456ef

The item supports interactive movement using the mouse. By clicking on the item and then dragging, the item will move together with the mouse cursor. If the item has children, all children are also moved. If the item is part of a selection, all selected items are also moved. This feature is provided as a convenience through the base implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`'s mouse event handlers.
