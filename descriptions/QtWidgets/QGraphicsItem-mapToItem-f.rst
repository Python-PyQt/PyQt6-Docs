.. sip:method-description::
    :status: todo
    :pysig: c777325c7558331d41fb7b28e96dc95d
    :realsig: (const QGraphicsItem*,const QPointF&) const
    :digest: b22c6826cbd4a483422bb59aebd7397b

Maps the point *point*, which is in this item's coordinate system, to *item*'s coordinate system, and returns the mapped coordinate.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
