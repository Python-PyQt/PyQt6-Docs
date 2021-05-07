.. sip:class-description::
    :status: todo
    :brief: Represents a single slice in a pie series
    :digest: ccf1fa299a30320f9a83d5eef5ca79c6

The :sip:ref:`~PyQt6.QtCharts.QPieSlice` class represents a single slice in a pie series.

A pie slice has a value and a label. When the slice is added to a pie series, the :sip:ref:`~PyQt6.QtCharts.QPieSeries` object calculates the percentage of the slice compared with the sum of all slices in the series to determine the actual size of the slice in the chart.

By default, the label is hidden. If it is visible, it can be either located outside the slice and connected to it with an arm or centered inside the slice either horizontally or in parallel with the tangential or normal of the slice's arc.

By default, the visual appearance of the slice is set by a theme, but the theme can be overridden by specifying slice properties. However, if the theme is changed after the slices are customized, all customization will be lost.

To enable user interaction with the pie chart, some basic signals are emitted when users click pie slices or hover the mouse over them.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QPieSeries`.
