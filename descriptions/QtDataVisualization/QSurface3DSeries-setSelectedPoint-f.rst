.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint&)
    :digest: 3b72e5741642c6017756d2b95c523663

Selects a surface grid point at the position *position* in the data array of the series specified by a row and a column.

Only one point can be selected at a time.

To clear selection from this series, :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries.invalidSelectionPosition` is set as *position*. If this series is added to a graph, the graph can adjust the selection according to user interaction or if it becomes invalid.

Removing rows from or inserting rows to the series before the row of the selected point will adjust the selection so that the same point will stay selected.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries.selectedPoint`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.clearSelection`.
