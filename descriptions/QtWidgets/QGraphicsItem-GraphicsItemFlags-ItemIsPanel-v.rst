.. sip:enum-member-description::
    :status: todo
    :value: 0x4000
    :realname: QGraphicsItem::GraphicsItemFlag::ItemIsPanel
    :digest: 762b2fcbf7e89368a241c184fe54534a

The item is a panel. A panel provides activation and contained focus handling. Only one panel can be active at a time (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isActive`). When no panel is active, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` activates all non-panel items. Window items (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isWindow` returns ``true``) are panels. This flag was introduced in Qt 4.6.
