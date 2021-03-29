.. sip:method-description::
    :status: todo
    :pysig: 7c0574595c80995729d7956d73f9fa01
    :realsig: (const QTransform&,bool)
    :digest: 7278a67f5489cfc8e2ac6ccdc2caa59a

Sets the item's current transformation matrix to *matrix*.

If *combine* is true, then *matrix* is combined with the current matrix; otherwise, *matrix* *replaces* the current matrix. *combine* is false by default.

To simplify interaction with items using a transformed view, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` provides mapTo... and mapFrom... functions that can translate between items' and the scene's coordinates. For example, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToScene` to map an item coordiate to a scene coordinate, or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromScene` to map from scene coordinates to item coordinates.

The transformation matrix is combined with the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformations` into a combined transformation that maps the item's coordinate system to its parent.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_, :ref:`Transformations<qgraphicsitem-transformations>`.
