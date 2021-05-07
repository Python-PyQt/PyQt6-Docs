.. sip:enum-description::
    :status: todo
    :realname: QGraphicsItem::GraphicsItemFlag
    :digest: 094c909e1d8bf3a5b8281bbd2243bfef

This enum describes different flags that you can set on an item to toggle different features in the item's behavior.

All flags are disabled by default.

**Note:** This flag is similar to  but in addition enforces the containment by clipping the children.

**Note:** With this flag set you can still scale the item itself, and that scale transformation will influence the item's children.

**Note:** If both this flag and  are set, the clip will be enforced. This is equivalent to just setting .

This flag was introduced in Qt 5.4.
