.. sip:method-description::
    :status: todo
    :pysig: 1e2e46ea1294f73ccddda57bc3636678
    :realsig: (const QPolygonF&, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform&) const
    :digest: 28e5ea96351fbcfe394905051485490b

Returns all visible items that, depending on *mode*, are either inside or intersect with the specified *polygon*, in a list sorted using *order*. In this case, "visible" defines items for which: isVisible() returns ``true``, effectiveOpacity() returns a value greater than 0.0 (which is fully transparent) and the parent item does not clip it.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *polygon* are returned.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemAt`, Sorting.
