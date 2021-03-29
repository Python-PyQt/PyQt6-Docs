.. sip:enum-member-description::
    :status: todo
    :value: 29
    :digest: 227c1ce4cffa7c10ab8c99d0bc52a06a

The item's rotation property has changed. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and after the item's rotation property has changed. The value argument is the new rotation (i.e., a double), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` ignores the return value for this notification (i.e., a read-only notification). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered.
