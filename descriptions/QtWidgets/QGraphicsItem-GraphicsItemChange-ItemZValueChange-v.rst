.. sip:enum-member-description::
    :status: todo
    :value: 23
    :digest: c619e55daaf77c0f8cc488cd955fd0a9

The item's Z-value changes. The value argument is the new Z-value (i.e., a double). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setZValue` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. Instead, you can return a new Z-value from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
