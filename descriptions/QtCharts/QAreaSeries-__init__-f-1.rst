.. sip:method-description::
    :status: todo
    :pysig: 5a2579a72d58663693d1154a37eb357f
    :realsig: (QLineSeries*,QLineSeries*)
    :digest: 52a157c7e3eac00401adb1c30431afd3

Constructs an area series object that will be spanned between an *upperSeries* line and a *lowerSeries* line. If no *lowerSeries* is passed to the constructor, the x-axis is used as the lower bound instead.

The :sip:ref:`~PyQt6.QtCharts.QAreaSeries` does not own the upper or lower series, but the ownership stays with the caller. When the series object is added to :sip:ref:`~PyQt6.QtCharts.QChartView` or :sip:ref:`~PyQt6.QtCharts.QChart`, the instance ownership is transferred.
