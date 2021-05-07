.. sip:class-description::
    :status: todo
    :brief: Base proxy class for Q3DSurface
    :digest: 7ae994a8a9b4cdffab19a73ba0b122de

Base proxy class for :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface`.

:sip:ref:`~PyQt6.QtDataVisualization.QHeightMapSurfaceDataProxy` takes care of surface related height map data handling. It provides a way to give a height map to be visualized as a surface plot.

Since height maps do not contain values for X or Z axes, those values need to be given separately using :sip:ref:`~PyQt6.QtDataVisualization.QHeightMapSurfaceDataProxy.minXValue`, :sip:ref:`~PyQt6.QtDataVisualization.QHeightMapSurfaceDataProxy.maxXValue`, :sip:ref:`~PyQt6.QtDataVisualization.QHeightMapSurfaceDataProxy.minZValue`, and :sip:ref:`~PyQt6.QtDataVisualization.QHeightMapSurfaceDataProxy.maxZValue` properties. X-value corresponds to image horizontal direction and Z-value to the vertical. Setting any of these properties triggers asynchronous re-resolving of any existing height map.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy`, `Qt Data Visualization Data Handling <https://doc.qt.io/qt-6/qtdatavisualization-data-handling.html>`_.
