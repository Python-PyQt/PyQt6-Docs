.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (QPoint)
    :digest: 58d4c9f4fd1ba3b7b18f96abf3dbb2df

Selects the bar at the *position* position, specified as a row and column in the data array of the series.

Only one bar can be selected at a time.

To clear the selection from this series, :sip:ref:`~PyQt6.QtGraphs.QBar3DSeries.invalidSelectionPosition` is set as *position*.

If this series is added to a graph, the graph can adjust the selection according to user interaction or if it becomes invalid. Selecting a bar on another added series will also clear the selection.

Removing rows from or inserting rows into the series before the row of the selected bar will adjust the selection so that the same bar will stay selected.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QBar3DSeries.selectedBar`, :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DGraphsWidgetItem.clearSelection`.
