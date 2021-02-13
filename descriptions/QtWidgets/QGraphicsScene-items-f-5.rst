.. sip:method-description::
    :status: todo
    :pysig: 6b3228054232b2c687b4641da178ea7c
    :realsig: (qreal,qreal,qreal,qreal,Qt::ItemSelectionMode,Qt::SortOrder,const QTransform&) const
    :digest: 12d93c922de2d69febec47a4b789fa23

This is an overloaded function.

Returns all visible items that, depending on *mode*, are either inside or intersect with the rectangle defined by *x*, *y*, *w* and *h*, in a list sorted using *order*. In this case, "visible" defines items for which: isVisible() returns ``true``, effectiveOpacity() returns a value greater than 0.0 (which is fully transparent) and the parent item does not clip it.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.
