.. sip:class-description::
    :status: todo
    :brief: Adds values to a chart's axes
    :digest: 2d92248777f8f7f6a0e11c561f5278c3

The :sip:ref:`~PyQt6.QtCharts.QValueAxis` class adds values to a chart's axes.

A value axis can be set up to show an axis line with tick marks, grid lines, and shades. The values on the axis are drawn at the positions of tick marks.

The following example code illustrates how to use the :sip:ref:`~PyQt6.QtCharts.QValueAxis` class:

::

    QChartView *chartView = new QChartView;
    QLineSeries *series = new QLineSeries;
    // ...
    chartView->chart()->addSeries(series);

    QValueAxis *axisX = new QValueAxis;
    axisX->setRange(10, 20.5);
    axisX->setTickCount(10);
    axisX->setLabelFormat("%.2f");
    chartView->chart()->setAxisX(axisX, series);
