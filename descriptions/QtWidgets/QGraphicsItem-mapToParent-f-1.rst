.. sip:method-description::
    :status: todo
    :pysig: b399b2f867f14bc8146f7836e1a1d20b
    :realsig: (const QRectF&) const
    :digest: 47c2d18fa2a369bdfd43d62d6ab428f4

Maps the rectangle *rect*, which is in this item's coordinate system, to its parent's coordinate system, and returns the mapped rectangle as a polygon. If the item has no parent, *rect* will be mapped to the scene's coordinate system.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
