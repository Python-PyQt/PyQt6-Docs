.. sip:class-description::
    :status: todo
    :brief: Presents data in scatter charts
    :digest: ed9a7cba2de2a2dff418682b56219960

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

For more information, see `ScatterChart Example <https://doc.qt.io/qt-6/qtcharts-scatterchart-example.html>`_ and `Scatter Interactions Example <https://doc.qt.io/qt-6/qtcharts-scatterinteractions-example.html>`_.
