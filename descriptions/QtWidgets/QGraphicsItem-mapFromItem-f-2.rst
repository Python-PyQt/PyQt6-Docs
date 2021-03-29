.. sip:method-description::
    :status: todo
    :pysig: ffa55e994d9e3d94dd0a4903cd230bd1
    :realsig: (const QGraphicsItem*,const QPolygonF&) const
    :digest: ea92c3d1aeeaf3437c2dc427107ebef9

Maps the polygon *polygon*, which is in *item*'s coordinate system, to this item's coordinate system, and returns the mapped polygon.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
