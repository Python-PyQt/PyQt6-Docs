.. sip:class-description::
    :status: todo
    :brief: Presents data as candlesticks
    :digest: 111265407e221b803577aae90e58f0da

The :sip:ref:`~PyQt6.QtCharts.QCandlestickSeries` class presents data as candlesticks.

This class acts as a container for single candlestick items. Each item is drawn to its own category when using :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`. :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis` and :sip:ref:`~PyQt6.QtCharts.QValueAxis` can be used as alternatives to :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`. In this case, each candlestick item is drawn according to its timestamp value.

**Note:** The timestamps must be unique within a :sip:ref:`~PyQt6.QtCharts.QCandlestickSeries`. When using :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`, only the first one of the candlestick items sharing a timestamp is drawn. If the chart includes multiple instances of :sip:ref:`~PyQt6.QtCharts.QCandlestickSeries`, items from different series sharing a timestamp are drawn to the same category. When using :sip:ref:`~PyQt6.QtCharts.QValueAxis` or :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis`, candlestick items sharing a timestamp will overlap each other.

See the `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_ to learn how to create a candlestick chart.

.. image:: ../../../images/examples_candlestickchart.png

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QCandlestickSet`, :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`, :sip:ref:`~PyQt6.QtCharts.QDateTimeAxis`, :sip:ref:`~PyQt6.QtCharts.QValueAxis`.
