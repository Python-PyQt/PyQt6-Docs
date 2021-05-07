.. sip:class-description::
    :status: todo
    :brief: Represents a data series in a 3D scatter graph
    :digest: 889934edaca79f869fc45c9d025c4434

The :sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries` class represents a data series in a 3D scatter graph.

This class manages the series specific visual elements, as well as the series data (via a data proxy).

If no data proxy is set explicitly for the series, the series creates a default proxy. Setting another proxy will destroy the existing proxy and all data added to it.

:sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries` supports the following format tags for :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DSeries.setItemLabelFormat`:

+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @xTitle     | Title from x-axis                                                                                                                                 |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @yTitle     | Title from y-axis                                                                                                                                 |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @zTitle     | Title from z-axis                                                                                                                                 |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @xLabel     | Item value formatted using the format of the x-axis. For more information, see :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.setLabelFormat`. |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @yLabel     | Item value formatted using the format of the y-axis. For more information, see :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.setLabelFormat`. |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @zLabel     | Item value formatted using the format of the z-axis. For more information, see :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.setLabelFormat`. |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| @seriesName | Name of the series                                                                                                                                |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

For example:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_qtdatavisualization.py
    :lines: 37-37

.. seealso:: `Qt Data Visualization Data Handling <https://doc.qt.io/qt-6/qtdatavisualization-data-handling.html>`_.
