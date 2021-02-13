.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b6b74108c1904e1268c7aa0def2bd919

This signal is emitted by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` whenever the selection changes. You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectedItems` to get the new list of selected items.

The selection changes whenever an item is selected or unselected, a selection area is set, cleared or otherwise changed, if a preselected item is added to the scene, or if a selected item is removed from the scene.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` emits this signal only once for group selection operations. For example, if you set a selection area, select or unselect a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup`, or if you add or remove from the scene a parent item that contains several selected items,  is emitted only once after the operation has completed (instead of once for each item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setSelectionArea`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectedItems`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setSelected`.
