.. sip:enum-member-description::
    :status: todo
    :value: 0x200
    :realname: QGraphicsItem::GraphicsItemFlag::ItemUsesExtendedStyleOption
    :digest: adc75d5d4cebe130406c39ac7708025d

The item makes use of either exposedRect in :sip:ref:`~PyQt6.QtWidgets.QStyleOptionGraphicsItem`. By default, the exposedRect is initialized to the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`. You can enable this flag for the style options to be set up with more fine-grained values. Use :sip:ref:`~PyQt6.QtWidgets.QStyleOptionGraphicsItem.levelOfDetailFromTransform` if you need a higher value. This flag was introduced in Qt 4.6.
