.. sip:method-description::
    :status: todo
    :pysig: 0da62cc17b663d7865b6c62be20d2ffc
    :realsig: (const QPolygon&, Qt::ItemSelectionMode) const
    :digest: a5b31570bffa4366c535075be7bbfd99

Returns a list of all the items that, depending on *mode*, are either contained by or intersect with *polygon*. *polygon* is in viewport coordinates.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *polygon* are returned.

The items are sorted by descending stacking order (i.e., the first item in the returned list is the uppermost item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene`, Sorting.
