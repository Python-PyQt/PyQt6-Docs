.. sip:method-description::
    :status: todo
    :pysig: 42c7a4ac47324c9f30028a85f2ecaca1
    :realsig: (const QGraphicsItem*,const QRectF&) const
    :digest: 8b24b943234d920d812d3503f62beeaa

Maps the rectangle *rect*, which is in this item's coordinate system, to *item*'s coordinate system, and returns the mapped rectangle as a new rectangle (i.e., the bounding rectangle of the resulting polygon).

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapRectToScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
