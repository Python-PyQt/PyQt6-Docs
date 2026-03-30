.. sip:class-description::
    :status: todo
    :brief: Allows presenting customized graph types
    :digest: ba37155ed6782d77bb6197f25c2149c5

The :sip:ref:`~PyQt6.QtGraphs.QCustomSeries` class allows presenting customized graph types.

Use :sip:ref:`~PyQt6.QtGraphs.QCustomSeries` to create customized graphs. Think of it as a scatter graph that lets you access custom data for each element.

:sip:ref:`~PyQt6.QtGraphs.QCustomSeries` defines a delegate that is used to render every item added to the graph. Each item includes user-defined data stored in a QVariantMap. Index of the item in the graph is also automatically added to the data map. The series passes this map to each element created based on the delegate. The delegate determines how to use the data.

To map data to the render coordinates defined by the ``QGraphsView`` axes, use the :sip:ref:`~PyQt6.QtGraphs.QCustomSeries.mapX` and :sip:ref:`~PyQt6.QtGraphs.QCustomSeries.mapY` functions.

**Note:** Currently, individual elements in a custom series do not share information with one another. For this reason, you can't implement a custom line series.
