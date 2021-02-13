.. sip:method-description::
    :status: todo
    :pysig: 42c7a4ac47324c9f30028a85f2ecaca1
    :realsig: (const QGraphicsItem*,const QRectF&) const
    :digest: 9241145b0631a906d9c9d5d1c3c28483

Maps the rectangle *rect*, which is in *item*'s coordinate system, to this item's coordinate system, and returns the mapped rectangle as a new rectangle (i.e., the bounding rectangle of the resulting polygon).

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapRectFromScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
