.. sip:method-description::
    :status: todo
    :pysig: 5e3824a1c5fe915a7229ee518b61f30c
    :realsig: (const QGraphicsItem*, Qt::ItemSelectionMode) const
    :digest: c102e952ddf3745505e580251a8e9a38

Returns a list of all items that collide with *item*. Collisions are determined by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem`; the collision detection is determined by *mode*. By default, all items whose shape intersects *item* or is contained inside *item*'s shape are returned.

The items are returned in descending stacking order (i.e., the first item in the list is the uppermost item, and the last item is the lowermost item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem`, Sorting.
