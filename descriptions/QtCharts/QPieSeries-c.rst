.. sip:class-description::
    :status: todo
    :brief: Presents data in pie charts
    :digest: 146e6dc651c28d601e759bca9d3534cb

The :sip:ref:`~PyQt6.QtCharts.QPieSeries` class presents data in pie charts.

A pie series consists of slices that are defined as :sip:ref:`~PyQt6.QtCharts.QPieSlice` objects. The slices can have any values as the :sip:ref:`~PyQt6.QtCharts.QPieSeries` object calculates the percentage of a slice compared with the sum of all slices in the series to determine the actual size of the slice in the chart.

Pie size and position on the chart are controlled by using relative values that range from 0.0 to 1.0. These relate to the actual chart rectangle.

By default, the pie is defined as a full pie. A partial pie can be created by setting a starting angle and angle span for the series. A full pie is 360 degrees, where 0 is at 12 a'clock.

See the `pie chart example <https://doc.qt.io/qt-6/qtcharts-piechart-example.html>`_ or `donut chart example <https://doc.qt.io/qt-6/qtcharts-donutchart-example.html>`_ to learn how to use :sip:ref:`~PyQt6.QtCharts.QPieSeries`.

.. image:: ../../../images/examples_piechart.png

.. image:: ../../../images/examples_donutchart.png

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QPieSlice`, :sip:ref:`~PyQt6.QtCharts.QChart`.
