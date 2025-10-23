.. sip:method-description::
    :status: todo
    :pysig: 01f154300f8d0c66615fa32b588de05f
    :realsig: (qreal, qreal, qreal, qreal, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform&) const
    :digest: b23d70ec5c6975f0b49ee0ccf1df5c54

Returns all visible items that, depending on *mode*, are either inside or intersect with the rectangle defined by *x*, *y*, *w* and *h*, in a list sorted using *order*. In this case, "visible" defines items for which: isVisible() returns ``true``, effectiveOpacity() returns a value greater than 0.0 (which is fully transparent) and the parent item does not clip it.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.
