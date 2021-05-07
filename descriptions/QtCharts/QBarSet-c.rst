.. sip:class-description::
    :status: todo
    :brief: Represents one set of bars in a bar chart
    :digest: 25dbddedb61aa6923a59d42fc2e90924

The :sip:ref:`~PyQt6.QtCharts.QBarSet` class represents one set of bars in a bar chart.

A bar set contains one data value for each category. The first value of a set is assumed to belong to the first category, the second one to the second category, and so on. If the set has fewer values than there are categories, the missing values are assumed to be located at the end of the set. For missing values in the middle of a set, the numerical value of zero is used. Labels for zero value sets are not shown.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries`, :sip:ref:`~PyQt6.QtCharts.QBarSeries`, :sip:ref:`~PyQt6.QtCharts.QStackedBarSeries`, :sip:ref:`~PyQt6.QtCharts.QPercentBarSeries`, :sip:ref:`~PyQt6.QtCharts.QHorizontalBarSeries`, :sip:ref:`~PyQt6.QtCharts.QHorizontalStackedBarSeries`, :sip:ref:`~PyQt6.QtCharts.QHorizontalPercentBarSeries`.
