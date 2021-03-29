.. sip:method-description::
    :status: todo
    :pysig: 03febbf03d579939d84ddb712d0e73c0
    :realsig: (const QPointF&,const QTransform&) const
    :digest: 62f77b4e3845340b06d5dd0242b6fc2c

Returns the topmost visible item at the specified *position*, or ``nullptr`` if there are no items at this position.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.collidingItems`, Sorting.
