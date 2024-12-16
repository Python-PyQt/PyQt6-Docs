.. sip:class-description::
    :status: todo
    :brief: Represents a data series in a 3D scatter graph
    :digest: 7d4eb57d5f7d4909d39de9549613ab31

The :sip:ref:`~PyQt6.QtGraphs.QScatter3DSeries` class represents a data series in a 3D scatter graph.

This class manages the series-specific visual elements, as well as the series data (via a data proxy).

Regarding the proxy-series relationship, it is crucial to highlight a couple of key points. In this context, data is stored in series and users can access the dataset through the series. This series is controlled or represented by a proxy object. Thus, the proxy can be used to manage various operations on the data and update the actual dataset. However, it is necessary to create a series associated with this proxy to edit the dataset.

If no data proxy is set explicitly for the series, the series creates a default proxy. Setting another proxy will destroy the existing proxy and all data added to the series.

:sip:ref:`~PyQt6.QtGraphs.QScatter3DSeries` supports the following format tags for :sip:ref:`~PyQt6.QtGraphs.QAbstract3DSeries.setItemLabelFormat`:

+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @xTitle     | Title from x-axis                                                                                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @yTitle     | Title from y-axis                                                                                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @zTitle     | Title from z-axis                                                                                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @xLabel     | Item value formatted using the format of the x-axis. For more information, see :sip:ref:`~PyQt6.QtGraphs.QValue3DAxis.labelFormat`. |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @yLabel     | Item value formatted using the format of the y-axis. For more information, see :sip:ref:`~PyQt6.QtGraphs.QValue3DAxis.labelFormat`. |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @zLabel     | Item value formatted using the format of the z-axis. For more information, see :sip:ref:`~PyQt6.QtGraphs.QValue3DAxis.labelFormat`. |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| @seriesName | Name of the series                                                                                                                  |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+

For example:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qtgraphs.py
    :lines: 11-11

.. seealso:: `Qt Graphs Data Handling with 3D <https://doc.qt.io/qt-6/qtgraphs-data-handling.html>`_.
