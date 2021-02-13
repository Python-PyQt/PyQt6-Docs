.. sip:method-description::
    :status: todo
    :pysig: 6d3883f70a4c67d84888a2fe66bdf981
    :realsig: (const QGraphicsItem*,Qt::ItemSelectionMode) const
    :digest: a3bac84de686f502ac4e742098cddc2f

Returns ``true`` if this item collides with *other*; otherwise returns ``false``.

The *mode* is applied to *other*, and the resulting shape or bounding rectangle is then compared to this item's shape. The default value for *mode* is :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`; *other* collides with this item if it either intersects, contains, or is contained by this item's shape (see :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` for details).

The default implementation is based on shape intersection, and it calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape` on both items. Because the complexity of arbitrary shape-shape intersection grows with an order of magnitude when the shapes are complex, this operation can be noticably time consuming. You have the option of reimplementing this function in a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` to provide a custom algorithm. This allows you to make use of natural constraints in the shapes of your own items, in order to improve the performance of the collision detection. For instance, two untransformed perfectly circular items' collision can be determined very efficiently by comparing their positions and radii.

Keep in mind that when reimplementing this function and calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` on *other*, the returned coordinates must be mapped to this item's coordinate system before any intersection can take place.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`.
