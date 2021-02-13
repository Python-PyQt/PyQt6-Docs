.. sip:method-description::
    :status: todo
    :pysig: f9bd8a5f055eed5f64fa9de087d09211
    :realsig: (const QGraphicsItem*,const QRectF&) const
    :digest: 6c8f46dcb65c154dad22fe481d8f0c5a

Maps the rectangle *rect*, which is in *item*'s coordinate system, to this item's coordinate system, and returns the mapped rectangle as a polygon.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene`

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
