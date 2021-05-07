.. sip:enum-member-description::
    :status: todo
    :value: 0x10
    :digest: a0d19dc38a7d00778b7648810b7d6c74

The item clips the painting of all its descendants to its own shape. Items that are either direct or indirect children of this item cannot draw outside this item's shape. By default, this flag is disabled; children can draw anywhere. This behavior is enforced by  or . This flag was introduced in Qt 4.3.
