.. sip:enum-member-description::
    :status: todo
    :value: 25
    :digest: eb0184506e6d62570a74686ca01b377d

The item's opacity changes. The value argument is the new opacity (i.e., a double). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setOpacity` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. Instead, you can return a new opacity from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
