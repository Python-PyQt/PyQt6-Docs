.. sip:method-description::
    :status: todo
    :pysig: 70fdb46d124e02d8a4f903d26e7c1cfc
    :realsig: (const QPointF&) const
    :digest: d24f623f415f95525450fc87a83862b4

Returns true if this item contains *point*, which is in local coordinates; returns false otherwise.

This function can be overwritten in order to handle point collisions in items with custom shapes. The default implementation checks if the point is inside the item's bounding rect.

Note that this method is generally used to check whether the item is under the mouse cursor, and for that reason, the implementation of this function should be as light-weight as possible.
