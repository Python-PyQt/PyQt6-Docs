.. sip:class-description::
    :status: todo
    :brief: Represents a data series in a 3D bar graph
    :digest: ed3c9b69f23f2a4396c85b33d4b1ac87

The :sip:ref:`~PyQt6.QtGraphs.QBar3DSeries` class represents a data series in a 3D bar graph.

This class manages the series specific visual elements, as well as the series data (via a data proxy).

Regarding the proxy-series relationship, it is crucial to highlight a couple of key points. In this context, data is stored in series and users can access the dataset through the series. This series is controlled or represented by a proxy object. Thus, the proxy can be used to manage various operations on the data and update the actual dataset. However, it is necessary to create a series associated with this proxy to edit the dataset.

If no data proxy is set explicitly for the series, the series creates a default proxy. Setting another proxy will destroy the existing proxy and all data added to the series.

:sip:ref:`~PyQt6.QtGraphs.QBar3DSeries` supports the following format tags for :sip:ref:`~PyQt6.QtGraphs.QAbstract3DSeries.setItemLabelFormat`:

+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @rowTitle      | Title from row axis                                                                                                                                           |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @colTitle      | Title from column axis                                                                                                                                        |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @valueTitle    | Title from value axis                                                                                                                                         |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @rowIdx        | Visible row index. Localized using the graph locale.                                                                                                          |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @colIdx        | Visible column index. Localized using the graph locale.                                                                                                       |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @rowLabel      | Label from row axis                                                                                                                                           |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @colLabel      | Label from column axis                                                                                                                                        |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @valueLabel    | Item value formatted using the format of the value axis attached to the graph. For more information, see :sip:ref:`~PyQt6.QtGraphs.QValue3DAxis.labelFormat`. |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| @seriesName    | Name of the series                                                                                                                                            |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %<format spec> | Item value in the specified format. Formatted using the same rules as :sip:ref:`~PyQt6.QtGraphs.QValue3DAxis.labelFormat`.                                    |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

For example:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qtgraphs.py
    :lines: 7-7

.. seealso:: `Qt Graphs Data Handling with 3D <https://doc.qt.io/qt-6/qtgraphs-data-handling.html>`_, :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DGraphsWidgetItem.locale`.
