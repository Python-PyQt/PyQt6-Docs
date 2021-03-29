.. sip:method-description::
    :status: todo
    :pysig: 28a048a93edb15adda812ab103ed5173
    :realsig: (const QTransform&) const
    :digest: 85a8cbebac593ced8ff8dda84e143a0e

Returns the bounding region for this item. The coordinate space of the returned region depends on *itemToDeviceTransform*. If you pass an identity :sip:ref:`~PyQt6.QtGui.QTransform` as a parameter, this function will return a local coordinate region.

The bounding region describes a coarse outline of the item's visual contents. Although it's expensive to calculate, it's also more precise than :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`, and it can help to avoid unnecessary repainting when an item is updated. This is particularly efficient for thin items (e.g., lines or simple polygons). You can tune the granularity for the bounding region by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setBoundingRegionGranularity`. The default granularity is 0; in which the item's bounding region is the same as its bounding rect.

*itemToDeviceTransform* is the transformation from item coordinates to device coordinates. If you want this function to return a :sip:ref:`~PyQt6.QtGui.QRegion` in scene coordinates, you can pass :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneTransform` as an argument.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRegionGranularity`.
