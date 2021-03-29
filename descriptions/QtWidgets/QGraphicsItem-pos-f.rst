.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: e465e5260ce7692434693db0aea3b3c0

Returns the position of the item in parent coordinates. If the item has no parent, its position is given in scene coordinates.

The position of the item describes its origin (local coordinate (0, 0)) in parent coordinates; this function returns the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToParent`\ (0, 0).

For convenience, you can also call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scenePos` to determine the item's position in scene coordinates, regardless of its parent.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.x`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.y`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setPos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_.
