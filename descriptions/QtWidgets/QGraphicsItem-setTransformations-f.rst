.. sip:method-description::
    :status: todo
    :pysig: 0f5c48e6552308791248670ad6242fa4
    :realsig: (const QList<QGraphicsTransform*>&)
    :digest: 8f64eb8ff21c03391d8dc0fadd26a0fe

Sets a list of graphics *transformations* (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform`) that currently apply to this item.

If all you want is to rotate or scale an item, you should call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale` instead. If you want to set an arbitrary transformation on an item, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` is for applying and controlling a chain of individual transformation operations on an item. It's particularly useful in animations, where each transform operation needs to be interpolated independently, or differently.

The transformations are combined with the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform` to map the item's coordinate system to the parent item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformations`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`, :ref:`Transformations<qgraphicsitem-transformations>`.
