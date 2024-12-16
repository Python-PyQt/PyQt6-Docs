.. sip:class-description::
    :status: todo
    :brief: Model mapper for line, spline, and scatter series
    :digest: 594e40e9eee0d216b5511243ae01f7c3

The :sip:ref:`~PyQt6.QtGraphs.QXYModelMapper` class is a model mapper for line, spline, and scatter series.

Model mappers enable using a data model derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class as a data source for a graph. A model mapper is used to create a connection between a line, spline, or scatter series. A *TableModel* is a natural choice for the model.

Both model and series properties can be used to manipulate the data. The model mapper keeps the series and the data model in sync.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QXYSeries`.
