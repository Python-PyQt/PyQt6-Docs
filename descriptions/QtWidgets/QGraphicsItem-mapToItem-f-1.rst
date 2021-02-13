.. sip:method-description::
    :status: todo
    :pysig: f9bd8a5f055eed5f64fa9de087d09211
    :realsig: (const QGraphicsItem*,const QRectF&) const
    :digest: 6d199c1180693bbb17e1cc5d9ef144f4

Maps the rectangle *rect*, which is in this item's coordinate system, to *item*'s coordinate system, and returns the mapped rectangle as a polygon.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
