.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 4dd0ec9212330172d6611d998a6917ef

The item's visible state changes. If the item is presently visible, it will become invisible, and vice verca. The value argument is the new visible state (i.e., true or false). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setVisible` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new visible state from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
