.. sip:enum-description::
    :status: todo
    :digest: 8791ff207df62e9f6e2f68e4d6cc2b78

This enum describes different flags that you can set on an item to toggle different features in the item's behavior.

All flags are disabled by default.

**Note:** This flag is similar to ItemContainsChildrenInShape but in addition enforces the containment by clipping the children.

**Note:** With this flag set you can still scale the item itself, and that scale transformation will influence the item's children.

**Note:** If both this flag and ItemClipsChildrenToShape are set, the clip will be enforced. This is equivalent to just setting ItemClipsChildrenToShape.

This flag was introduced in Qt 5.4.
