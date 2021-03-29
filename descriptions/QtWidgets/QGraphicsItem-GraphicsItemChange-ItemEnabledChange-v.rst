.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: c8f73f4a81a60a6e500bfaa95e7d2366

The item's enabled state changes. If the item is presently enabled, it will become disabled, and vice verca. The value argument is the new enabled state (i.e., true or false). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setEnabled` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. Instead, you can return the new state from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
