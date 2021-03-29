.. sip:method-description::
    :status: todo
    :pysig: ffa55e994d9e3d94dd0a4903cd230bd1
    :realsig: (const QGraphicsItem*,const QPolygonF&) const
    :digest: d93468f696ad049c79a842aa5a797d2f

Maps the polygon *polygon*, which is in this item's coordinate system, to *item*'s coordinate system, and returns the mapped polygon.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
