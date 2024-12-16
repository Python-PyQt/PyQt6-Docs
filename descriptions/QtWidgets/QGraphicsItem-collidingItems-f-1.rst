.. sip:method-description::
    :status: todo
    :pysig: e4383cdd4bf7c4d10a2de62f383aff00
    :realsig: (Qt::ItemSelectionMode) const
    :digest: 6aa96a867b679e454b501365d1e86be5

Returns a list of all items that collide with this item.

The way collisions are detected is determined by applying *mode* to items that are compared to this item, i.e., each item's shape or bounding rectangle is checked against this item's shape. The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem`.
