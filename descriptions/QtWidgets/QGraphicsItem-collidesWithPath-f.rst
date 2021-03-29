.. sip:method-description::
    :status: todo
    :pysig: 02940f13b020cb19b917587873057589
    :realsig: (const QPainterPath&,Qt::ItemSelectionMode) const
    :digest: 62b64328692468d375520bb48b81fe05

Returns ``true`` if this item collides with *path*.

The collision is determined by *mode*. The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; *path* collides with this item if it either intersects, contains, or is contained by this item's shape.

Note that this function checks whether the item's shape or bounding rectangle (depending on *mode*) is contained within *path*, and not whether *path* is contained within the items shape or bounding rectangle.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`.
