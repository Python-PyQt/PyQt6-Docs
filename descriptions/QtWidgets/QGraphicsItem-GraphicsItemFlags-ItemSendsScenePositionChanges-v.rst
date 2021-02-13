.. sip:enum-member-description::
    :status: todo
    :value: 0x10000
    :realname: QGraphicsItem::GraphicsItemFlag::ItemSendsScenePositionChanges
    :digest: b19a006c9d4c35ad9a9a6bcff8c36433

The item enables :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` notifications for :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemScenePositionHasChanged`. For performance reasons, these notifications are disabled by default. You must enable this flag to receive notifications for scene position changes. This flag was introduced in Qt 4.6.
