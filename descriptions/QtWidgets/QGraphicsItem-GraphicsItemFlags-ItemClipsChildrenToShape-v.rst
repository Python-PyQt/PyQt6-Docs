.. sip:enum-member-description::
    :status: todo
    :value: 0x10
    :realname: QGraphicsItem::GraphicsItemFlag::ItemClipsChildrenToShape
    :digest: 9b383c41744a9cca2490ab0281ee70a1

The item clips the painting of all its descendants to its own shape. Items that are either direct or indirect children of this item cannot draw outside this item's shape. By default, this flag is disabled; children can draw anywhere. This behavior is enforced by QGraphicsView::drawItems() or QGraphicsScene::drawItems(). This flag was introduced in Qt 4.3.
