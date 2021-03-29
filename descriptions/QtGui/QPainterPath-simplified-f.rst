.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: 1551dbfb17dd44498824d8b5144d2c40

Returns a simplified version of this path. This implies merging all subpaths that intersect, and returning a path containing no intersecting edges. Consecutive parallel lines will also be merged. The simplified path will always use the default fill rule, :sip:ref:`~PyQt6.QtCore.Qt.FillRule.OddEvenFill`. Bezier curves may be flattened to line segments due to numerical instability of doing bezier curve intersections.
