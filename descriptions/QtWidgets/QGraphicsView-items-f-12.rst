.. sip:method-description::
    :status: todo
    :pysig: 1af8de7bdd12978c4565c3d282ee7582
    :realsig: (const QPainterPath&, Qt::ItemSelectionMode) const
    :digest: 11e8d72274a93c673ee2367ea27ba555

This is an overloaded function.

Returns a list of all the items that, depending on *mode*, are either contained by or intersect with *path*. *path* is in viewport coordinates.

The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; all items whose exact shape intersects with or is contained by *path* are returned.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene`, Sorting.
