.. sip:class-description::
    :status: todo
    :brief: Presents data in scatter charts
    :digest: 49df62a5e488724418aad07258109e35

The :sip:ref:`~PyQt6.QtCharts.QScatterSeries` class presents data in scatter charts.

The scatter data is displayed as a collection of points on the chart. For each point, two values are specified that determine its position on the horizontal axis and the vertical axis.

.. image:: ../../../images/examples_scatterchart.png

The following code snippet illustrates how to create a basic scatter chart:

::

    QScatterSeries* series = new QScatterSeries();
    series->append(0, 6);
    series->append(2, 4);
    ...
    chart->addSeries(series);

For more information, see `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_ and `Creating Scatter Charts <https://doc.qt.io/qt-6/qtcharts-scatterchart-example.html>`_.
