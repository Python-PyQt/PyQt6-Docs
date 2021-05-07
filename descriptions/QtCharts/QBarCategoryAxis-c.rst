.. sip:class-description::
    :status: todo
    :brief: Adds categories to a chart's axes
    :digest: 71a273ca1623f2cff856f0ba863778e0

The :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis` class adds categories to a chart's axes.

:sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis` can be set up to show an axis line with tick marks, grid lines, and shades. Categories are drawn between the ticks. It can be used also with a line series, as demonstrated by the `Line and BarChart Example <https://doc.qt.io/qt-6/qtcharts-lineandbar-example.html>`_.

The following code illustrates how to use :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`:

::

    QChartView *chartView = new QChartView;
    QBarSeries *series = new QBarSeries;
    // ...
    chartView->chart()->addSeries(series);
    chartView->chart()->createDefaultAxes();

    QBarCategoryAxis *axisX = new QBarCategoryAxis;
    QStringList categories;
    categories << "Jan" << "Feb" << "Mar" << "Apr" << "May" << "Jun";
    axisX->append(categories);
    axisX->setRange("Feb", "May");
    chartView->chart()->setAxisX(axisX, series);
