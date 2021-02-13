.. sip:method-description::
    :status: todo
    :pysig: b0b4073c9da8b90ee4f49e6dfa6a9192
    :realsig: (const QTransform&) const
    :digest: 5f2babbb083e12e5a6399da9c64b8ff7

Converts the path into a list of polygons using the :sip:ref:`~PyQt6.QtGui.QTransform` *matrix*, and returns the list.

The function differs from the :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon` function in that it creates several polygons. It is provided because it is usually faster to draw several small polygons than to draw one large polygon, even though the total number of points drawn is the same.

The  function differs from the :sip:ref:`~PyQt6.QtGui.QPainterPath.toSubpathPolygons` function in that it create only polygon for subpaths that have overlapping bounding rectangles.

Like the :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon` function, this function uses a rewinding technique to make sure that overlapping subpaths can be filled using the correct fill rule. Note that rewinding inserts addition lines in the polygons so the outline of the fill polygon does not match the outline of the path.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.toSubpathPolygons`, :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon`, QPainterPath Conversion.
