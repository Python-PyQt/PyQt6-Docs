.. sip:class-description::
    :status: todo
    :brief: Presents data in box-and-whiskers charts
    :digest: 385efa821ae96eec56c4f50e83763803

The :sip:ref:`~PyQt6.QtCharts.QBoxPlotSeries` class presents data in box-and-whiskers charts.

A box plot series acts as a container for box-and-whiskers items. Items from multiple series are grouped into categories according to their index value.

The :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis` class is used to add the categories to the chart's axis. Category labels have to be unique. If the same category label is defined for several box-and-whiskers items, only the first one is drawn.

See the `box-and-whiskers chart example <https://doc.qt.io/qt-6/qtcharts-boxplotchart-example.html>`_ to learn how to create a box-and-whiskers chart.

.. image:: ../../../images/examples_boxplotchart.png

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QBoxSet`, :sip:ref:`~PyQt6.QtCharts.QBarCategoryAxis`.
