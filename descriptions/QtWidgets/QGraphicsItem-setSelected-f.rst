.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 4a98b25fcf2050ffebb27eff2cde2500

If *selected* is true and this item is selectable, this item is selected; otherwise, it is unselected.

If the item is in a group, the whole group's selected state is toggled by this function. If the group is selected, all items in the group are also selected, and if the group is not selected, no item in the group is selected.

Only visible, enabled, selectable items can be selected. If *selected* is true and this item is either invisible or disabled or unselectable, this function does nothing.

By default, items cannot be selected. To enable selection, set the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsSelectable` flag.

This function is provided for convenience, allowing individual toggling of the selected state of an item. However, a more common way of selecting items is to call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setSelectionArea`, which will call this function for all visible, enabled, and selectable items within a specified area on the scene.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isSelected`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectedItems`.
