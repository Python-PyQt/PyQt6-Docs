.. sip:class-description::
    :status: todo
    :brief: The data proxy for a 3D bars graph
    :digest: 2fc54a6d73263afc106e2bdbbf41cf29

The :sip:ref:`~PyQt6.QtDataVisualization.QBarDataProxy` class is the data proxy for a 3D bars graph.

A bar data proxy handles adding, inserting, changing, and removing rows of data.

The data array is a list of vectors (rows) of :sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem` instances. Each row can contain a different number of items or even be null.

:sip:ref:`~PyQt6.QtDataVisualization.QBarDataProxy` takes ownership of all QtDataVisualization::QBarDataRow objects passed to it, whether directly or in a QtDataVisualization::QBarDataArray container. If bar data row pointers are used to directly modify data after adding the array to the proxy, the appropriate signal must be emitted to update the graph.

:sip:ref:`~PyQt6.QtDataVisualization.QBarDataProxy` optionally keeps track of row and column labels, which :sip:ref:`~PyQt6.QtDataVisualization.QCategory3DAxis` can utilize to show axis labels. The row and column labels are stored in a separate array from the data and row manipulation methods provide alternate versions that do not affect the row labels. This enables the option of having row labels that relate to the position of the data in the array rather than the data itself.

.. seealso:: `Qt Data Visualization Data Handling <https://doc.qt.io/qt-6/qtdatavisualization-data-handling.html>`_.
