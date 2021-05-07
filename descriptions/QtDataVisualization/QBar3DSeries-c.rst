.. sip:class-description::
    :status: todo
    :brief: Represents a data series in a 3D bar graph
    :digest: 69627e0b20ef5270685b9c28799e59b6

The :sip:ref:`~PyQt6.QtDataVisualization.QBar3DSeries` class represents a data series in a 3D bar graph.

This class manages the series specific visual elements, as well as the series data (via a data proxy).

If no data proxy is set explicitly for the series, the series creates a default proxy. Setting another proxy will destroy the existing proxy and all data added to it.

:sip:ref:`~PyQt6.QtDataVisualization.QBar3DSeries` supports the following format tags for :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DSeries.setItemLabelFormat`:

+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @rowTitle      | Title from row axis                                                                                                                                                      |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @colTitle      | Title from column axis                                                                                                                                                   |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @valueTitle    | Title from value axis                                                                                                                                                    |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @rowIdx        | Visible row index. Localized using the graph locale.                                                                                                                     |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @colIdx        | Visible column index. Localized using the graph locale.                                                                                                                  |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @rowLabel      | Label from row axis                                                                                                                                                      |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @colLabel      | Label from column axis                                                                                                                                                   |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @valueLabel    | Item value formatted using the format of the value axis attached to the graph. For more information, see :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.labelFormat`. |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @seriesName    | Name of the series                                                                                                                                                       |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %<format spec> | Item value in the specified format. Formatted using the same rules as :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.labelFormat`.                                    |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For example:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_qtdatavisualization.py
    :lines: 37-37

.. seealso:: `Qt Data Visualization Data Handling <https://doc.qt.io/qt-6/qtdatavisualization-data-handling.html>`_, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.locale`.
