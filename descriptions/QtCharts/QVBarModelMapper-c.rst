.. sip:class-description::
    :status: todo
    :brief: Vertical model mapper for bar series
    :digest: ef431e67764c6f2b37f75f1b9b29943e

The :sip:ref:`~PyQt6.QtCharts.QVBarModelMapper` class is a vertical model mapper for bar series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A vertical model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries`, so that each column in the data model defines a bar set and each row maps to a category in a bar series.

Both model and bar series properties can be used to manipulate the data. The model mapper keeps the bar series and the data model in sync.

The model mapper ensures that all the bar sets in the bar series have equal sizes. Therefore, adding or removing a value from a bar set causes the same change to be made in all the bar sets in the bar series.

For more information, see `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QHBarModelMapper`.
