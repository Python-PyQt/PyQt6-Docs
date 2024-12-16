.. sip:method-description::
    :status: todo
    :pysig: f5a93ef6a1b0cb0fdc41b38d9fb9c98b
    :realsig: () const
    :digest: 50736b8f5fbbf2df89ba14743d2f23e3

Returns a list of graphics transforms that currently apply to this item.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` is for applying and controlling a chain of individual transformation operations on an item. It's particularly useful in animations, where each transform operation needs to be interpolated independently, or differently.

The transformations are combined with the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform` to map the item's coordinate system to the parent item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformations`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformOriginPoint`, :ref:`qgraphicsitem-transformations`.
