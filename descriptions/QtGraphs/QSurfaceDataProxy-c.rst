.. sip:class-description::
    :status: todo
    :brief: The data proxy for a 3D surface graph
    :digest: 1a989077cd025be747d8e55fd22b3c10

The :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy` class is the data proxy for a 3D surface graph.

A surface data proxy handles surface related data in rows. For this it provides two auxiliary type aliases: QtGraphs::QSurfaceDataArray and QtGraphs::QSurfaceDataRow. ``QSurfaceDataArray`` is a QList that controls the rows. ``QSurfaceDataRow`` is a QList that contains :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem` objects. For more information about how to feed the data to the proxy, see the sample code in the :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DSurfaceWidgetItem` documentation. Since data is stored in series, it is necessary to create a series associated with the proxy before using these functions for the dataset.

All rows must have the same number of items.

:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy` takes ownership of all ``QSurfaceDataRow`` objects passed to it, whether directly or in a ``QSurfaceDataArray`` container. To use surface data row pointers to directly modify data after adding the array to the proxy, the appropriate signal must be emitted to update the graph.

To make a sensible surface, the x-value of each successive item in all rows must be either ascending or descending throughout the row. Similarly, the z-value of each successive item in all columns must be either ascending or descending throughout the column.

**Note:** Currently only surfaces with straight rows and columns are fully supported. Any row with items that do not have the exact same z-value or any column with items that do not have the exact same x-value may get clipped incorrectly if the whole surface does not completely fit within the visible x-axis or z-axis ranges.

**Note:** Surfaces with less than two rows or columns are not considered valid surfaces and will not be rendered.

**Note:** On some environments, surfaces with a lot of visible vertices may not render, because they exceed the per-draw vertex count supported by the graphics driver. This is mostly an issue on 32-bit and OpenGL ES2 platforms.

.. seealso:: `Qt Graphs Data Handling with 3D <https://doc.qt.io/qt-6/qtgraphs-data-handling.html>`_.
