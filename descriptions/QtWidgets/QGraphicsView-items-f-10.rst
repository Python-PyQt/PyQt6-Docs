.. sip:method-description::
    :status: todo
    :pysig: f3795d01f84cbb9e2c21990eb790a04c
    :realsig: (const QRect&, Qt::ItemSelectionMode) const
    :digest: 009cb6b05b4d844f32efff0573ccea17

Returns a list of all the items that, depending on *mode*, are either contained by or intersect with *rect*. *rect* is in viewport coordinates.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *rect* are returned.

The items are sorted in descending stacking order (i.e., the first item in the returned list is the uppermost item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene`, Sorting.
