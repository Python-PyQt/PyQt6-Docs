.. sip:enum-member-description::
    :status: todo
    :value: 0x80000
    :digest: 55d327f43f1c28a4acd79f6d59ffe3c1

This flag indicates that all of the item's direct or indirect children only draw within the item's shape. Unlike , this restriction is not enforced. Set  when you manually assure that drawing is bound to the item's shape and want to avoid the cost associated with enforcing the clip. Setting this flag enables more efficient drawing and collision detection. The flag is disabled by default.
