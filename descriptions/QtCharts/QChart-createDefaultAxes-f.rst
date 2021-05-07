.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a0609b98ce89cc5668395b8ea462074d

Creates axes for the chart based on the series that have already been added to the chart. Any axes previously added to the chart will be deleted.

**Note:** This function has to be called after all series have been added to the chart. The axes created by this function will NOT get automatically attached to any series added to the chart after this function has been called. A series with no axes attached will by default scale to utilize the entire plot area of the chart, which can be confusing if there are other series with properly attached axes also present.

+---------------------------------------+---------------------------------------------+---------------------------------------+
| Series type                           | Horizontal axis (X)                         | Vertical axis (Y)                     |
+=======================================+=============================================+=======================================+
| :sip:ref:`~PyQt6.QtCharts.QXYSeries`  | :sip:ref:`~PyQt6.QtCharts.QValueAxis`       | :sip:ref:`~PyQt6.QtCharts.QValueAxis` |
+---------------------------------------+---------------------------------------------+---------------------------------------+
| :sip:ref:`~PyQt6.QtCharts.QBarSeries` | :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis` | :sip:ref:`~PyQt6.QtCharts.QValueAxis` |
+---------------------------------------+---------------------------------------------+---------------------------------------+
| :sip:ref:`~PyQt6.QtCharts.QPieSeries` | None                                        | None                                  |
+---------------------------------------+---------------------------------------------+---------------------------------------+

If there are several :sip:ref:`~PyQt6.QtCharts.QXYSeries` derived series added to the chart and no series of other types have been added, then only one pair of axes is created. If there are several series of different types added to the chart, then each series gets its own axes pair.

The axes specific to the series can be later obtained from the chart by providing the series as the parameter for the :sip:ref:`~PyQt6.QtCharts.QChart.axes` function call. :sip:ref:`~PyQt6.QtCharts.QPieSeries` does not create any axes.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QChart.axes`, :sip:ref:`~PyQt6.QtCharts.QAbstractSeries.attachAxis`.
