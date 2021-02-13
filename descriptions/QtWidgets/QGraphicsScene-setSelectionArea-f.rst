.. sip:method-description::
    :status: todo
    :pysig: b51273ef6a2c5b0c298cabac8db5577f
    :realsig: (const QPainterPath&,const QTransform&)
    :digest: 01fa5d3301bc88f0640b84840d2d1c51

Sets the selection area to *path*. All items within this area are immediately selected, and all items outside are unselected. You can get the list of all selected items by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectedItems`.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

For an item to be selected, it must be marked as *selectable* (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsSelectable`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.clearSelection`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectionArea`.
