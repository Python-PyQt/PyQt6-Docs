.. sip:class-description::
    :status: todo
    :brief: Presents data in polar charts
    :digest: cdbdec4412573325aecc7464af67c868

The :sip:ref:`~PyQt6.QtCharts.QPolarChart` presents data in polar charts.

Polar charts present data in a circular graph, where the placement of data is based on the angle and distance from the center of the graph, the *pole*.

.. image:: ../../../images/examples_polarchart.png

A polar chart is a specialization of :sip:ref:`~PyQt6.QtCharts.QChart` that supports line, spline, area, and scatter series, and all axis types supported by them. Each axis can be used either as a radial or an angular axis.

The first and last tick mark on an angular :sip:ref:`~PyQt6.QtCharts.QValueAxis` are co-located at a 0/360 degree angle.

If the angular distance between two consecutive points in a series is more than 180 degrees, any direct line connecting the two points becomes meaningless, and will not be drawn. Instead, a line will be drawn to and from the center of the chart. Therefore, the axis ranges must be chosen accordingly when displaying line, spline, or area series.

Polar charts draw all axes of the same orientation in the same position, so using multiple axes of the same orientation can be confusing, unless the extra axes are only used to customize the grid. For example, you can display a highlighted range with a secondary shaded :sip:ref:`~PyQt6.QtCharts.QCategoryAxis` or provide unlabeled subticks with a secondary :sip:ref:`~PyQt6.QtCharts.QValueAxis` thas has hidden labels.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QChart`.
