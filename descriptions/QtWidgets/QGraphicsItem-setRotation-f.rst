.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: c5899af717451be84c141dc1aa63477b

Sets the clockwise rotation *angle*, in degrees, around the Z axis. The default value is 0 (i.e., the item is not rotated). Assigning a negative value will rotate the item counter-clockwise. Normally the rotation angle is in the range (-360, 360), but it's also possible to assign values outside of this range (e.g., a rotation of 370 degrees is the same as a rotation of 10 degrees).

The item is rotated around its transform origin point, which by default is (0, 0). You can select a different transformation origin by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`.

The rotation is combined with the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformations` to map the item's coordinate system to the parent item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`, :ref:`Transformations<qgraphicsitem-transformations>`.
