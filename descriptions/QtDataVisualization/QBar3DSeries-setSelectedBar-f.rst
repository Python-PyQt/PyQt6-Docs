.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint&)
    :digest: 9e04bbafb2451efe1a2834ff512f1260

Selects the bar at the *position* position, specified as a row and column in the data array of the series.

Only one bar can be selected at a time.

To clear selection from this series, :sip:ref:`~PyQt6.QtDataVisualization.QBar3DSeries.invalidSelectionPosition` is set as *position*.

If this series is added to a graph, the graph can adjust the selection according to user interaction or if it becomes invalid. Selecting a bar on another added series will also clear the selection.

Removing rows from or inserting rows to the series before the row of the selected bar will adjust the selection so that the same bar will stay selected.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QBar3DSeries.selectedBar`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.clearSelection`.
