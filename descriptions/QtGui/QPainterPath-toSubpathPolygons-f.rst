.. sip:method-description::
    :status: todo
    :pysig: b0b4073c9da8b90ee4f49e6dfa6a9192
    :realsig: (const QTransform&) const
    :digest: 44d64b3c24885882d9cda1d0e6ffd4e4

Converts the path into a list of polygons using the :sip:ref:`~PyQt6.QtGui.QTransform` *matrix*, and returns the list.

This function creates one polygon for each subpath regardless of intersecting subpaths (i.e. overlapping bounding rectangles). To make sure that such overlapping subpaths are filled correctly, use the :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygons` function instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygons`, :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon`, QPainterPath Conversion.
