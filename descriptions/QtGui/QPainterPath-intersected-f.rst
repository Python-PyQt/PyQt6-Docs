.. sip:method-description::
    :status: todo
    :pysig: 7d38cafd49881113072a25f94c4fa5b3
    :realsig: (const QPainterPath&) const
    :digest: e19a054bb949ad69f1f21e81c98f9bbe

Returns a path which is the intersection of this path's fill area and *p*'s fill area. Bezier curves may be flattened to line segments due to numerical instability of doing bezier curve intersections.
