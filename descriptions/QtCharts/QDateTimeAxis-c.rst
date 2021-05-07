.. sip:class-description::
    :status: todo
    :brief: Adds dates and times to a chart's axis
    :digest: 4d3e70d43d0d114a885e486b10b2bf7d

The :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis` class adds dates and times to a chart's axis.

:sip:ref:`~PyQt6.QtCharts.QDateTimeAxis` can be set up to show an axis line with tick marks, grid lines, and shades. The labels can be configured by setting an appropriate DateTime format. :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis` works correctly with dates from 4714 BCE to 287396 CE. For other limitiations related to :sip:ref:`~PyQt6.QtCore.QDateTime`, see :sip:ref:`~PyQt6.QtCore.QDateTime` documentation.

**Note:** :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis` is disabled on platforms that define qreal as float.

.. image:: ../../../images/api_datatime_axis.png

:sip:ref:`~PyQt6.QtCharts.QDateTimeAxis` can be used with any :sip:ref:`~PyQt6.QtCharts.QXYSeries`. To add a data point to the series, :sip:ref:`~PyQt6.QtCore.QDateTime.toMSecsSinceEpoch` is used:

::

    QLineSeries *series = new QLineSeries;

    QDateTime xValue;
    xValue.setDate(QDate(2012, 1 , 18));
    xValue.setTime(QTime(9, 34));
    qreal yValue = 12;
    series->append(xValue.toMSecsSinceEpoch(), yValue);

    xValue.setDate(QDate(2013, 5 , 11));
    xValue.setTime(QTime(11, 14));
    qreal yValue = 22;
    series->append(xValue.toMSecsSinceEpoch(), yValue);

The following code snippet illustrates adding the series to the chart and setting up :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis`:

::

    QChartView *chartView = new QChartView;
    chartView->chart()->addSeries(series);

    // ...
    QDateTimeAxis *axisX = new QDateTimeAxis;
    axisX->setFormat("dd-MM-yyyy h:mm");
    chartView->chart()->setAxisX(axisX, series);
