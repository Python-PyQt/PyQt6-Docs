.. sip:class-description::
    :status: todo
    :brief: Presents a series of categorized data as a percentage of each category
    :digest: b7abd266fb44aed7147a75caad7abb26

The :sip:ref:`~PyQt6.QtCharts.QPercentBarSeries` class presents a series of categorized data as a percentage of each category.

This class draws data as a series of uniformly sized vertically stacked bars, with one bar per category. Each bar set added to the series contributes a single segment to each stacked bar. The segment size corresponds to the percentage of the segment value compared with the total value of all segments in the stack. Bars with zero value are not drawn.

See the `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_ to learn how to create a percent bar chart.

.. image:: ../../../images/examples_percentbarchart.png

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QBarSet`, :sip:ref:`~PyQt6.QtCharts.QStackedBarSeries`, :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries`.
