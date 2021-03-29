.. sip:method-description::
    :status: todo
    :pysig: c3e2a1177bc43b6575b1f3f9176f3109
    :realsig: (const QGraphicsItem*,const QPainterPath&) const
    :digest: 5e76fc0d6f57ae8066d8176faf3c5530

Maps the path *path*, which is in *item*'s coordinate system, to this item's coordinate system, and returns the mapped path.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
