.. sip:method-description::
    :status: todo
    :pysig: b6da2bfae229ab0448ace11dffdc01bb
    :realsig: (const QPointF&) const
    :digest: 137f6dd01a6504be59002735b3a078ac

Maps the point *point*, which is in this item's coordinate system, to its parent's coordinate system, and returns the mapped coordinate. If the item has no parent, *point* will be mapped to the scene's coordinate system.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
