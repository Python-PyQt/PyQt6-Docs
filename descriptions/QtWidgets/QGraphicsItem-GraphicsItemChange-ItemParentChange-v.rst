.. sip:enum-member-description::
    :status: todo
    :value: 5
    :digest: 46f03578a2191a732e0b2ae9c96dda93

The item's parent changes. The value argument is the new parent item (i.e., a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` pointer). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setParentItem` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new parent from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
