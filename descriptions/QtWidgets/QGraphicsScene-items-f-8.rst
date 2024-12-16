.. sip:method-description::
    :status: todo
    :pysig: e506b20090e25103f0bf8ae4446ff42f
    :realsig: (const QRectF&, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform&) const
    :digest: d4e4f728aab67d41a0d2e1815ea4788a

This is an overloaded function.

Returns all visible items that, depending on *mode*, are either inside or intersect with the specified *rect*, in a list sorted using *order*. In this case, "visible" defines items for which: isVisible() returns ``true``, effectiveOpacity() returns a value greater than 0.0 (which is fully transparent) and the parent item does not clip it.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *rect* are returned.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemAt`, Sorting.
