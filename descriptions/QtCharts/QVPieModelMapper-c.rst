.. sip:class-description::
    :status: todo
    :brief: Vertical model mapper for pie series
    :digest: 5649a3bfdaba7f2c70dfced28f1bf427

The :sip:ref:`~PyQt6.QtCharts.QVPieModelMapper` is a vertical model mapper for pie series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A vertical model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtCharts.QPieSeries`, so that each row in the data model defines a pie slice and each column maps to the label or the value of the pie slice.

Both model and pie series properties can be used to manipulate the data. The model mapper keeps the pie series and the data model in sync.
