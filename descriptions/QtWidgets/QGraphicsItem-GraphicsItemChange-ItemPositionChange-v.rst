.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: b0713b94576209730381aef4fd687b94

The item's position changes. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and when the item's local position changes, relative to its parent (i.e., as a result of calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setPos` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.moveBy`). The value argument is the new position (i.e., a :sip:ref:`~PyQt6.QtCore.QPointF`). You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.pos` to get the original position. Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setPos` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.moveBy` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new, adjusted position from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`. After this notification, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` immediately sends the  notification if the position changed.
