.. sip:method-description::
    :status: todo
    :pysig: 7d38cafd49881113072a25f94c4fa5b3
    :realsig: (const QPainterPath&) const
    :digest: f8a050ae5e4013564f3a3c33e6eba4dc

Maps the path *path*, which is in this item's coordinate system, to its parent's coordinate system, and returns the mapped path. If the item has no parent, *path* will be mapped to the scene's coordinate system.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
