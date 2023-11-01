.. sip:class-description::
    :status: todo
    :brief: Abstract parent class for all bar series classes
    :digest: 2012db1597276a6c34aebbbbb1ead4e1

The :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries` class is an abstract parent class for all bar series classes.

In bar charts, bars are defined as bar sets that contain one data value for each category. The position of a bar is specified by the category and its height by the data value. Bar series that contain multiple bar sets group together bars that belong to the same category. The way the bars are displayed is determined by the subclass of this class chosen to create the bar chart.

If a :sip:ref:`~PyQt6.QtCharts.QValueAxis` is used instead of :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis` for the main bar axis, the bars are grouped around the index value of the category.

See the `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_ to learn how to use the :sip:ref:`~PyQt6.QtCharts.QBarSeries` class to create a simple bar chart.

.. image:: ../../../images/examples_barchart.png

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QBarSet`, :sip:ref:`~PyQt6.QtCharts.QBarSeries`, :sip:ref:`~PyQt6.QtCharts.QStackedBarSeries`, :sip:ref:`~PyQt6.QtCharts.QPercentBarSeries`, :sip:ref:`~PyQt6.QtCharts.QHorizontalBarSeries`, :sip:ref:`~PyQt6.QtCharts.QHorizontalStackedBarSeries`, :sip:ref:`~PyQt6.QtCharts.QHorizontalPercentBarSeries`.
