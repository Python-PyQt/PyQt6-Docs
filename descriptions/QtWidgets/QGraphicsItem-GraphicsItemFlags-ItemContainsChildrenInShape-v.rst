.. sip:enum-member-description::
    :status: todo
    :value: 0x80000
    :realname: QGraphicsItem::GraphicsItemFlag::ItemContainsChildrenInShape
    :digest: 06357d5ee04c3e6496b752515d3fcf1e

This flag indicates that all of the item's direct or indirect children only draw within the item's shape. Unlike ItemClipsChildrenToShape, this restriction is not enforced. Set ItemContainsChildrenInShape when you manually assure that drawing is bound to the item's shape and want to avoid the cost associated with enforcing the clip. Setting this flag enables more efficient drawing and collision detection. The flag is disabled by default.
