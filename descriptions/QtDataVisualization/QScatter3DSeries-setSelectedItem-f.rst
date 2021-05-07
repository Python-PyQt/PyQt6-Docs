.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ffd71d9cb1c6f9f697e0e5a522c410cb

Selects the item at the index *index* in the data array of the series. Only one item can be selected at a time.

To clear selection from this series, :sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries.invalidSelectionIndex` is set as *index*. If this series is added to a graph, the graph can adjust the selection according to user interaction or if it becomes invalid. Selecting an item on another added series will also clear the selection.

Removing items from or inserting items to the series before the selected item will adjust the selection so that the same item will stay selected.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries.selectedItem`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.clearSelection`.
