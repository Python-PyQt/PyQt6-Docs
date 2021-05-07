.. sip:class-description::
    :status: todo
    :brief: Horizontal model mapper for bar series
    :digest: d8f8e307fb23e061a3de21c2d555e23f

The :sip:ref:`~PyQt6.QtCharts.QHBarModelMapper` class is a horizontal model mapper for bar series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A horizontal model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries`, so that each row in the data model defines a bar set and each column maps to a category in a bar series.

Both model and bar series properties can be used to manipulate the data. The model mapper keeps the bar series and the data model in sync.

The model mapper ensures that all the bar sets in the bar series have equal sizes. Therefore, adding or removing a value from a bar set causes the same change to be made in all the bar sets in the bar series.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QVBarModelMapper`.
