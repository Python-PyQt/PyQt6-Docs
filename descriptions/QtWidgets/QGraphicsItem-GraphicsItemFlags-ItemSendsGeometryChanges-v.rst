.. sip:enum-member-description::
    :status: todo
    :value: 0x800
    :realname: QGraphicsItem::GraphicsItemFlag::ItemSendsGeometryChanges
    :digest: 8c997809aa817a1b1ed276117a96a576

The item enables :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` notifications for :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformChange`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformHasChanged`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemRotationChange`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemRotationHasChanged`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemScaleChange`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemScaleHasChanged`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformOriginPointChange`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformOriginPointHasChanged`. For performance reasons, these notifications are disabled by default. You must enable this flag to receive notifications for position and transform changes. This flag was introduced in Qt 4.6.
