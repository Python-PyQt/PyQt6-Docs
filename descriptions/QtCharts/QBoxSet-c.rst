.. sip:class-description::
    :status: todo
    :brief: Represents one item in a box-and-whiskers chart
    :digest: 18a5b687cd777ab4479c5f70df8897f0

The :sip:ref:`~PyQt6.QtCharts.QBoxSet` class represents one item in a box-and-whiskers chart.

A box-and-whiskers item is a graphical representation of a range and three median values that is constructed from five different values. There are two ways to specify the values. The first one is by using a constructor or stream operator (<<). The values have to be specified in the following order: lower extreme, lower quartile, median, upper quartile, and upper extreme.

The second way is to create an empty :sip:ref:`~PyQt6.QtCharts.QBoxSet` instance and specify the values using the :sip:ref:`~PyQt6.QtCharts.QBoxSet.setValue` method.

See the `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_ to learn how to create a box-and-whiskers chart.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QBoxPlotSeries`.
