.. sip:method-description::
    :status: todo
    :pysig: c3e2a1177bc43b6575b1f3f9176f3109
    :realsig: (const QGraphicsItem*,const QPainterPath&) const
    :digest: 4c79041e71dec4664ca4531e4c6d0255

Maps the path *path*, which is in this item's coordinate system, to *item*'s coordinate system, and returns the mapped path.

If *item* is ``nullptr``, this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
