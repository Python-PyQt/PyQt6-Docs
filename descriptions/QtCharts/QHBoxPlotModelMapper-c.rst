.. sip:class-description::
    :status: todo
    :brief: Horizontal model mapper for box plot series
    :digest: cb168173e1cd488f47b97931904955bc

The :sip:ref:`~PyQt6.QtCharts.QHBoxPlotModelMapper` class is a horizontal model mapper for box plot series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A horizontal model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtCharts.QBoxPlotSeries` object, so that each row in the data model defines a box-and-whiskers item and each column maps to the range and three median values of the box-and-whiskers item.

Both model and series properties can be used to manipulate the data. The model mapper keeps the series and the data model in sync.

The model mapper ensures that all the box-and-whiskers items in the box plot series have equal sizes. Therefore, adding or removing a value from a box-and-whiskers item causes the same change to be made in all the box-and-whiskers items in the box plot series.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QVBoxPlotModelMapper`.
