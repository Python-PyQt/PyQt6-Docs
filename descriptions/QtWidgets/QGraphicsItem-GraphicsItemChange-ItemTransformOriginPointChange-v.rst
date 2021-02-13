.. sip:enum-member-description::
    :status: todo
    :value: 32
    :digest: bff712d4fb5b3c6aa3905dc4c4e9521e

The item's transform origin point property changes. This notification is sent if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag is enabled, and when the item's transform origin point property changes (i.e., as a result of calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`). The value argument is the new origin point (i.e., a :sip:ref:`~PyQt6.QtCore.QPointF`); to get the old origin point, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformOriginPoint`. Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered; instead, you can return the new transform origin point from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
