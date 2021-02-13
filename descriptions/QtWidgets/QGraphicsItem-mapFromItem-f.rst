.. sip:method-description::
    :status: todo
    :pysig: c777325c7558331d41fb7b28e96dc95d
    :realsig: (const QGraphicsItem*,const QPointF&) const
    :digest: c9255f1d1e3c4ce6ab0a602c53957d13

Maps the point *point*, which is in *item*'s coordinate system, to this item's coordinate system, and returns the mapped coordinate.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
