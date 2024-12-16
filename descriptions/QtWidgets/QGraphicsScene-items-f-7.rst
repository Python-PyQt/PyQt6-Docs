.. sip:method-description::
    :status: todo
    :pysig: 0f5275e6b04a77f3ef38f2be235481be
    :realsig: (const QPointF&, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform&) const
    :digest: dbbf0628a83dd5b748d5cab174989021

Returns all visible items that, depending on *mode*, are at the specified *pos* in a list sorted using *order*. In this case, "visible" defines items for which: isVisible() returns ``true``, effectiveOpacity() returns a value greater than 0.0 (which is fully transparent) and the parent item does not clip it.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with *pos* are returned.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemAt`, Sorting.
