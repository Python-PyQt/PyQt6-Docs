.. sip:enum-description::
    :status: todo
    :realname: QGraphicsItem::GraphicsItemFlag
    :digest: 9013b1140d1ae4b9ad7746d5788cb38e

This enum describes different flags that you can set on an item to toggle different features in the item's behavior.

All flags are disabled by default.

**Note:** This flag is similar to  but in addition enforces the containment by clipping the children.

**Note:** With this flag set you can still scale the item itself, and that scale transformation will influence the item's children.

**Note:** If both this flag and  are set, the clip will be enforced. This is equivalent to just setting .

This flag was introduced in Qt 5.4.
