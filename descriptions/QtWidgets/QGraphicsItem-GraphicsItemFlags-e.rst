.. sip:enum-description::
    :status: todo
    :realname: QGraphicsItem::GraphicsItemFlag
    :digest: 32249b429c13192c6946454cef33066a

This enum describes different flags that you can set on an item to toggle different features in the item's behavior.

All flags are disabled by default.

**Note:** This flag is similar to  but in addition enforces the containment by clipping the children.

**Note:** With this flag set you can still scale the item itself, and that scale transformation will influence the item's children.

click focus to items underneath when being clicked on. This flag allows you create a non-focusable item that can be clicked on without changing the focus.

, but also suppresses focus-out. This flag allows you to completely take over focus handling. This flag was introduced in Qt 4.7.

**Note:** If both this flag and  are set, the clip will be enforced. This is equivalent to just setting .

This flag was introduced in Qt 5.4.
