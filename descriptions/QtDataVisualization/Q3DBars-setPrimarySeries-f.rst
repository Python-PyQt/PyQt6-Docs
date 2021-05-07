.. sip:method-description::
    :status: todo
    :pysig: 2a53c32b7367689680e9e0639e3209f0
    :realsig: (QBar3DSeries*)
    :digest: b16980c4a5b9345aa982ba630c5c29ab

Sets *series* as the primary series of the graph. The primary series determines the row and column axis labels when the labels are not explicitly set to the axes.

If the specified series is not yet added to the graph, setting it as the primary series will also implicitly add it to the graph.

If the primary series itself is removed from the graph, this property resets to default.

If *series* is null, this property resets to default. Defaults to the first added series or zero if no series are added to the graph.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.primarySeries`.
