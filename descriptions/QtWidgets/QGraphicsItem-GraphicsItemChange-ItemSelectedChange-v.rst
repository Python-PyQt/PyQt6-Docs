.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: b60b9482a86aad07338bb4455fc0dca8

The item's selected state changes. If the item is presently selected, it will become unselected, and vice verca. The value argument is the new selected state (i.e., true or false). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setSelected` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new selected state from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
