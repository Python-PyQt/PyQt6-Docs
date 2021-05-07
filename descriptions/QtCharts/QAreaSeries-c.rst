.. sip:class-description::
    :status: todo
    :brief: Presents data in area charts
    :digest: 9873f55cb4031ffefc865a0b0ba3b2b7

The :sip:ref:`~PyQt6.QtCharts.QAreaSeries` class presents data in area charts.

An area series is used to show quantitative data. It is based on a line series, in the way that the area between the boundary lines is emphasized with color. Since the area series is based on the line series, the :sip:ref:`~PyQt6.QtCharts.QAreaSeries` constructor needs a :sip:ref:`~PyQt6.QtCharts.QLineSeries` instance, which defines the *upper* boundary of the area. The area chart is drawn using the bottom of the plot area as the *lower* boundary by default. Instead of the bottom of the plot area, the lower boundary can be specified by another line. In that case, :sip:ref:`~PyQt6.QtCharts.QAreaSeries` should be initialized with two :sip:ref:`~PyQt6.QtCharts.QLineSeries` instances.

**Note:** The terms *upper* and *lower* boundary can be misleading in cases where the value of the lower boundary is greater than that of the upper boundary. The main point is that the area between these two boundary lines will be filled.

See the `area chart example <https://doc.qt.io/qt-6/qtcharts-areachart-example.html>`_ to learn how to create a simple area chart.

.. image:: ../../../images/examples_areachart.png
