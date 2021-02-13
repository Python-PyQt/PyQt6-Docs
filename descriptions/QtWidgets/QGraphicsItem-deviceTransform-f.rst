.. sip:method-description::
    :status: todo
    :pysig: cff1c4b576b241a7d3c7365c35e64e49
    :realsig: (const QTransform&) const
    :digest: 2c2ae5c96f716864bb5a473f03229a8e

Returns this item's device transformation matrix, using *viewportTransform* to map from scene to device coordinates. This matrix can be used to map coordinates and geometrical shapes from this item's local coordinate system to the viewport's (or any device's) coordinate system. To map coordinates from the viewport, you must first invert the returned matrix.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 112-119

This function is the same as combining this item's scene transform with the view's viewport transform, but it also understands the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIgnoresTransformations` flag. The device transform can be used to do accurate coordinate mapping (and collision detection) for untransformable items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scenePos`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemTransform`.
