.. sip:class-description::
    :status: todo
    :brief: Presents data in pie graphs
    :digest: 209df660ae1fd16782b9a5372e528a5b

The :sip:ref:`~PyQt6.QtGraphs.QPieSeries` class presents data in pie graphs.

A pie series consists of slices that are defined as :sip:ref:`~PyQt6.QtGraphs.QPieSlice` objects. The slices can have any values as the :sip:ref:`~PyQt6.QtGraphs.QPieSeries` object calculates the percentage of a slice compared with the sum of all slices in the series to determine the actual size of the slice in the graph.

Pie size and position on the graph are controlled by using relative values that range from 0.0 to 1.0. These relate to the actual graph rectangle.

By default, the pie is defined as a full pie. A partial pie can be created by setting a starting angle and angle span for the series. A full pie is 360 degrees, where 0 is at 12 a'clock.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QPieSlice`.
