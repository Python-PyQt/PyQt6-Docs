.. sip:method-description::
    :status: todo
    :pysig: 7d38cafd49881113072a25f94c4fa5b3
    :realsig: (const QPainterPath&) const
    :digest: b915537cff7d1e5f0146642cf6a37050

Returns a path which is *p*'s fill area subtracted from this path's fill area.

Set operations on paths will treat the paths as areas. Non-closed paths will be treated as implicitly closed. Bezier curves may be flattened to line segments due to numerical instability of doing bezier curve intersections.
