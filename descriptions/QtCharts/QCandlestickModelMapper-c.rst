.. sip:class-description::
    :status: todo
    :brief: Abstract model mapper class for candlestick series
    :digest: 7b6373c1e050430cbdcf848857530382

Abstract model mapper class for candlestick series.

Model mappers allow the use of a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`-derived model as a data source for a chart series, creating a connection between a :sip:ref:`~PyQt6.QtCharts.QCandlestickSeries` and the model object. A model mapper maintains an equal size across all :sip:ref:`~PyQt6.QtCharts.QCandlestickSet`.

**Note:** The model used must support adding and removing rows/columns and modifying the data of the cells.
