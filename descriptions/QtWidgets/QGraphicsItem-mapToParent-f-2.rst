.. sip:method-description::
    :status: todo
    :pysig: 4490a8d0e22b4e949f8cc6cb75745cd0
    :realsig: (const QPolygonF&) const
    :digest: d43a4e4475ffd8cdb1fbca62b7e8f8b9

Maps the polygon *polygon*, which is in this item's coordinate system, to its parent's coordinate system, and returns the mapped polygon. If the item has no parent, *polygon* will be mapped to the scene's coordinate system.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
