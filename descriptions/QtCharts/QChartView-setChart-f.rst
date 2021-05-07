.. sip:method-description::
    :status: todo
    :pysig: d5e4a9b780c90476a13d2cf59e0c41a0
    :realsig: (QChart*)
    :digest: 4f10a1943c02184304096dc7c276039f

Sets the current chart to *chart*. The ownership of the new chart is passed to the chart view and the ownership of the previous chart is released.

To avoid memory leaks, the previous chart must be deleted.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QChartView.chart`.
