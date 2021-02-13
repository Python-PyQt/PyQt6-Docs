.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 5f2167d0316390400ba30ef2d8b20131

Sets the Z-value of the item to *z*. The Z value decides the stacking order of sibling (neighboring) items. A sibling item of high Z value will always be drawn on top of another sibling item with a lower Z value.

If you restore the Z value, the item's insertion order will decide its stacking order.

The Z-value does not affect the item's size in any way.

The default Z-value is 0.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.zValue`, Sorting, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.stackBefore`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemStacksBehindParent`.
