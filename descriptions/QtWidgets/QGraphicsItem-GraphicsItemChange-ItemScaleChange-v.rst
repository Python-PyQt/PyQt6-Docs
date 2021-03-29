.. sip:enum-member-description::
    :status: todo
    :value: 30
    :digest: 6a197d9336920ae3a0f5223ef6f6a523

The item's scale property changes. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and when the item's scale property changes (i.e., as a result of calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale`). The value argument is the new scale (i.e., a double); to get the old scale, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale`. Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new scale from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
