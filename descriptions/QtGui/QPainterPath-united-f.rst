.. sip:method-description::
    :status: todo
    :pysig: 7d38cafd49881113072a25f94c4fa5b3
    :realsig: (const QPainterPath&) const
    :digest: 269eb16e55650b655113bc8af9275cbb

Returns a path which is the union of this path's fill area and *p*'s fill area.

Set operations on paths will treat the paths as areas. Non-closed paths will be treated as implicitly closed. Bezier curves may be flattened to line segments due to numerical instability of doing bezier curve intersections.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.intersected`, :sip:ref:`~PyQt6.QtGui.QPainterPath.subtracted`.
