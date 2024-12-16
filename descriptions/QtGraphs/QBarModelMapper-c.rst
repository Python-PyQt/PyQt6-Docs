.. sip:class-description::
    :status: todo
    :brief: Model mapper for bar series
    :digest: 42fbe64ca68b994ae2d59312a183293e

The :sip:ref:`~PyQt6.QtGraphs.QBarModelMapper` class is a model mapper for bar series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a graph. A model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtGraphs.QBarSeries`.

Both model and bar series properties can be used to manipulate the data. The model mapper keeps the bar series and the data model in sync.

The model mapper ensures that all the bar sets in the bar series have equal sizes. Therefore, adding or removing a value from a bar set causes the same change to be made in all the bar sets in the bar series.
