.. sip:class-description::
    :status: todo
    :brief: Base proxy class for Q3DSurfaceWidgetItem
    :digest: e4ee254cb818a734b170bcc5d42acd47

Base proxy class for :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DSurfaceWidgetItem`.

:sip:ref:`~PyQt6.QtGraphs.QHeightMapSurfaceDataProxy` takes care of the processing of height map data related to surfaces. It provides the visualization of a height map as a surface plot.

Since height maps do not contain values for X or Z axes, those values need to be given separately using the :sip:ref:`~PyQt6.QtGraphs.QHeightMapSurfaceDataProxy.minXValue`, :sip:ref:`~PyQt6.QtGraphs.QHeightMapSurfaceDataProxy.maxXValue`, :sip:ref:`~PyQt6.QtGraphs.QHeightMapSurfaceDataProxy.minZValue`, and :sip:ref:`~PyQt6.QtGraphs.QHeightMapSurfaceDataProxy.maxZValue` properties. The X-value corresponds to image horizontal direction and the Z-value to the vertical. Setting any of these properties triggers an asynchronous re-resolution of any existing height map.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy`, `Qt Graphs Data Handling with 3D <https://doc.qt.io/qt-6/qtgraphs-data-handling.html>`_.
