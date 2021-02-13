.. sip:enum-member-description::
    :status: todo
    :value: 19
    :digest: 80eb7074a9d7e477862daa6e46bd4164

The item's tooltip changes. The value argument is the new tooltip (i.e., a :sip:ref:`~PyQt6.QtWidgets.QToolTip`). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setToolTip` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. Instead, you can return a new tooltip from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
