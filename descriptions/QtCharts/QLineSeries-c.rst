.. sip:class-description::
    :status: todo
    :brief: Presents data in line charts
    :digest: 4ce408c677e0076f4571f514b0748a38

The :sip:ref:`~PyQt6.QtCharts.QLineSeries` class presents data in line charts.

A line chart is used to show information as a series of data points connected by straight lines.

.. image:: ../../../images/examples_linechart.png

Creating a basic line chart is simple:

::

    QLineSeries* series = new QLineSeries();
    series->append(0, 6);
    series->append(2, 4);
    ...
    chart->addSeries(series);
