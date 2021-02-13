.. sip:enum-member-description::
    :status: todo
    :value: 31
    :digest: 03c04af1b41fa1d96d372f2133ac0e04

The item's scale property has changed. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and after the item's scale property has changed. The value argument is the new scale (i.e., a double), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` ignores the return value for this notification (i.e., a read-only notification). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered.
