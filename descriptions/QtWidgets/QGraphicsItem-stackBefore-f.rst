.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (const QGraphicsItem*)
    :digest: 99af1f98dbcd46ca9848f43cb53a4150

Stacks this item before *sibling*, which means this item will be drawn behind the sibling item. In other words, the sibling item will visually appear on top of this item.

The two items must be siblings (i.e., they must share the same parent item, or must both be toplevel items).The *sibling* must have the same Z value as this item, otherwise calling this function will have no effect.

By default, all sibling items are stacked by insertion order (i.e., the first item you add is drawn before the next item you add). If two items' Z values are different, then the item with the highest Z value is drawn on top. When the Z values are the same, the insertion order will decide the stacking order.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setZValue`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemStacksBehindParent`, Sorting.
