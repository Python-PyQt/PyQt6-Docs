.. sip:enum-member-description::
    :status: todo
    :value: 33
    :digest: 8fc4f23f7a5031124213218320c997fd

The item's transform origin point property has changed. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and after the item's transform origin point property has changed. The value argument is the new origin point (i.e., a :sip:ref:`~PyQt6.QtCore.QPointF`), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` ignores the return value for this notification (i.e., a read-only notification). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered.
