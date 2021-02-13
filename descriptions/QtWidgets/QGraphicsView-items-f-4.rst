.. sip:method-description::
    :status: todo
    :pysig: a792444ae6ef53ca35b23fa313273829
    :realsig: (const QPolygon&,Qt::ItemSelectionMode) const
    :digest: f1fe639113fddcfb0a3936ec19969ec2

This is an overloaded function.

Returns a list of all the items that, depending on *mode*, are either contained by or intersect with *polygon*. *polygon* is in viewport coordinates.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *polygon* are returned.

The items are sorted by descending stacking order (i.e., the first item in the returned list is the uppermost item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene`, Sorting.
