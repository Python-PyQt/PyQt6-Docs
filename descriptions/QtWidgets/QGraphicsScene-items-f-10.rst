.. sip:method-description::
    :status: todo
    :pysig: 795fea532f6bcdbea5716a1e4aaaacbc
    :realsig: (const QPainterPath&, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform&) const
    :digest: c316a0079465bb0bf7218371dd45549f

This is an overloaded function.

Returns all visible items that, depending on *mode*, are either inside or intersect with the specified *path*, in a list sorted using *order*. In this case, "visible" defines items for which: isVisible() returns ``true``, effectiveOpacity() returns a value greater than 0.0 (which is fully transparent) and the parent item does not clip it.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *path* are returned.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemAt`, Sorting.
