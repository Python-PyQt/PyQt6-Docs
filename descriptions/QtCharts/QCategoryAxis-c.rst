.. sip:class-description::
    :status: todo
    :brief: Places named ranges on the axis
    :digest: 640a44a16fd0905e40fdb5dfa6c1d968

The :sip:ref:`~PyQt6.QtCharts.QCategoryAxis` class places named ranges on the axis.

This class can be used to explain the underlying data by adding labeled categories. Unlike :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`, :sip:ref:`~PyQt6.QtCharts.QCategoryAxis` allows the widths of the category ranges to be specified freely.

Example code on how to use :sip:ref:`~PyQt6.QtCharts.QCategoryAxis`:

.. image:: ../../../images/api_category_axis.png

::

    QChartView *chartView = new QChartView;
    QLineSeries *series = new QLineSeries;
    // ...
    chartView->chart()->addSeries(series);

    QCategoryAxis *axisY = new QCategoryAxis;
    axisY->setMin(0);
    axisY->setMax(52);
    axisY->setStartValue(15);
    axisY->append("First", 20);
    axisY->append("Second", 37);
    axisY->append("Third", 52);
    chartView->chart()->setAxisY(axisY, series);
