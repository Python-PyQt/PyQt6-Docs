.. sip:class-description::
    :status: todo
    :brief: Horizontal model mapper for pie series
    :digest: 0de1f2bec06081278df1484a1df89a13

The :sip:ref:`~PyQt6.QtCharts.QHPieModelMapper` is a horizontal model mapper for pie series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A horizontal model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtCharts.QPieSeries`, so that each column in the data model defines a pie slice and each row maps to the label or the value of the pie slice.

Both model and pie series properties can be used to manipulate the data. The model mapper keeps the pie series and the data model in sync.
