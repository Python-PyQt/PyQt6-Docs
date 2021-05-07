.. sip:method-description::
    :status: todo
    :pysig: c0ff2f69d960122911e0b1ff58417436
    :realsig: (QAbstractSeries*)
    :digest: 3541072ab9608ba75de52e197b113712

Adds the series *series* to the chart and takes ownership of it.

**Note:** A newly added series is not attached to any axes by default, not even those that might have been created for the chart using :sip:ref:`~PyQt6.QtCharts.QChart.createDefaultAxes` before the series was added to the chart. If no axes are attached to the newly added series before the chart is shown, the series will get drawn as if it had axes with ranges that exactly fit the series to the plot area of the chart. This can be confusing if the same chart also displays other series that have properly attached axes, so always make sure you either call :sip:ref:`~PyQt6.QtCharts.QChart.createDefaultAxes` after a series has been added or explicitly attach axes for the series.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QChart.removeSeries`, :sip:ref:`~PyQt6.QtCharts.QChart.removeAllSeries`, :sip:ref:`~PyQt6.QtCharts.QChart.createDefaultAxes`, :sip:ref:`~PyQt6.QtCharts.QAbstractSeries.attachAxis`.
