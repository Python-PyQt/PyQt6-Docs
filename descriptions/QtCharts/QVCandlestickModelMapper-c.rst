.. sip:class-description::
    :status: todo
    :brief: Vertical model mapper for a candlestick series
    :digest: 8e3b8faf3e394b50e3152bb74a753d33

The :sip:ref:`~PyQt6.QtCharts.QVCandlestickModelMapper` class is a vertical model mapper for a candlestick series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A vertical model mapper is used to create a connection between a data model and :sip:ref:`~PyQt6.QtCharts.QCandlestickSeries`, so that each column in the data model defines a candlestick item and each row maps to the open, high, low, close, and timestamp values of the candlestick item.

Both model and candlestick series properties can be used to manipulate the data. The model mapper keeps the candlestick series and the data model in sync.

The model mapper ensures that all the candlestick items in the candlestick series have equal sizes. Therefore, adding or removing a value from a candlestick item causes the same change to be made in all the candlestick items in the candlestick series.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QCandlestickSeries`, :sip:ref:`~PyQt6.QtCharts.QCandlestickSet`, :sip:ref:`~PyQt6.QtCharts.QHCandlestickModelMapper`.
