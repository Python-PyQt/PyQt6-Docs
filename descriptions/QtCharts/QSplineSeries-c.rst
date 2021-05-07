.. sip:class-description::
    :status: todo
    :brief: Presents data as spline charts
    :digest: d8e17736502ac04582446fba0b0c3cdf

The :sip:ref:`~PyQt6.QtCharts.QSplineSeries` class presents data as spline charts.

A spline series stores the data points and the segment control points needed by :sip:ref:`~PyQt6.QtGui.QPainterPath` to draw a spline. The control points are automatically calculated when the data changes. The algorithm computes the points so that the normal spline can be drawn.

.. image:: ../../../images/examples_splinechart.png

The following code snippet illustrates how to create a basic spline chart:

::

    QSplineSeries* series = new QSplineSeries();
    series->append(0, 6);
    series->append(2, 4);
    ...
    chart->addSeries(series);
