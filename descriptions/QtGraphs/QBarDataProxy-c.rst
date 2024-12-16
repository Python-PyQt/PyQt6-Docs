.. sip:class-description::
    :status: todo
    :brief: The data proxy for a 3D bars graph
    :digest: e518757bd0cbdda5da1797c1063f02b5

The :sip:ref:`~PyQt6.QtGraphs.QBarDataProxy` class is the data proxy for a 3D bars graph.

A bar data proxy handles adding, inserting, changing, and removing rows of data.

The data array is a list of vectors (rows) of :sip:ref:`~PyQt6.QtGraphs.QBarDataItem` instances. Each row can contain a different number of items or even be null.

:sip:ref:`~PyQt6.QtGraphs.QBarDataProxy` takes ownership of all QtGraphs::QBarDataRow objects passed to it, whether directly or in a QtGraphs::QBarDataArray container. If bar data row pointers are used to directly modify data after adding the array to the proxy, the appropriate signal must be emitted to update the graph.

:sip:ref:`~PyQt6.QtGraphs.QBarDataProxy` optionally keeps track of row and column labels, which :sip:ref:`~PyQt6.QtGraphs.QCategory3DAxis` can utilize to show axis labels.

The row and column labels are stored in a separate array from the data in the series rather. Row processing methods are available in the proxy and provide alternative versions that do not affect row labels. This enables the option of having row labels that relate to the position of the data in the array rather than the data itself. Since the series holds the data and row and column labels, it is necessary to create a series associated with the proxy before using these functions for them.

.. seealso:: `Qt Graphs Data Handling with 3D <https://doc.qt.io/qt-6/qtgraphs-data-handling.html>`_.
