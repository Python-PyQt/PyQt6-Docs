.. sip:method-description::
    :status: todo
    :pysig: b93f750e87e8104518204b5b81df775e
    :realsig: (const QRect&,Qt::ItemSelectionMode) const
    :digest: c7f3f27631dc2fbc207d1c971add13d0

This is an overloaded function.

Returns a list of all the items that, depending on *mode*, are either contained by or intersect with *rect*. *rect* is in viewport coordinates.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *rect* are returned.

The items are sorted in descending stacking order (i.e., the first item in the returned list is the uppermost item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene`, Sorting.
