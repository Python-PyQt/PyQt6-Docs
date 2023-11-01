.. sip:class-description::
    :status: todo
    :brief: Vertical model mapper for line, spline, and scatter series
    :digest: 8039d5297f8bfc133af57d55c2ffe309

The :sip:ref:`~PyQt6.QtCharts.QVXYModelMapper` class is a vertical model mapper for line, spline, and scatter series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a chart. A vertical model mapper is used to create a connection between a line, spline, or scatter series and the data model that has *X* and *Y* columns for the coordinates and holds the data points for the `XYSeries <https://doc.qt.io/qt-6/qml-qtcharts-xyseries.html>`_ as rows. A *TableModel* is a natural choice for the model.

Both model and series properties can be used to manipulate the data. The model mapper keeps the series and the data model in sync.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QHXYModelMapper`, :sip:ref:`~PyQt6.QtCharts.QXYSeries`, `Charts with Widgets Gallery <https://doc.qt.io/qt-6/qtcharts-chartsgallery-example.html>`_.
