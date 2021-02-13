.. sip:class-description::
    :status: todo
    :brief: Container for painting operations, enabling graphical shapes to be constructed and reused
    :digest: cabe95fdc2bbbefd71da799682111698

The :sip:ref:`~PyQt6.QtGui.QPainterPath` class provides a container for painting operations, enabling graphical shapes to be constructed and reused.

A painter path is an object composed of a number of graphical building blocks, such as rectangles, ellipses, lines, and curves. Building blocks can be joined in closed subpaths, for example as a rectangle or an ellipse. A closed path has coinciding start and end points. Or they can exist independently as unclosed subpaths, such as lines and curves.

A :sip:ref:`~PyQt6.QtGui.QPainterPath` object can be used for filling, outlining, and clipping. To generate fillable outlines for a given painter path, use the :sip:ref:`~PyQt6.QtGui.QPainterPathStroker` class. The main advantage of painter paths over normal drawing operations is that complex shapes only need to be created once; then they can be drawn many times using only calls to the :sip:ref:`~PyQt6.QtGui.QPainter.drawPath` function.

:sip:ref:`~PyQt6.QtGui.QPainterPath` provides a collection of functions that can be used to obtain information about the path and its elements. In addition it is possible to reverse the order of the elements using the :sip:ref:`~PyQt6.QtGui.QPainterPath.toReversed` function. There are also several functions to convert this painter path object into a polygon representation.

.. _qpainterpath-composing-a-qpainterpath:

Composing a QPainterPath
------------------------

A :sip:ref:`~PyQt6.QtGui.QPainterPath` object can be constructed as an empty path, with a given start point, or as a copy of another :sip:ref:`~PyQt6.QtGui.QPainterPath` object. Once created, lines and curves can be added to the path using the :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.arcTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.cubicTo` and :sip:ref:`~PyQt6.QtGui.QPainterPath.quadTo` functions. The lines and curves stretch from the :sip:ref:`~PyQt6.QtGui.QPainterPath.currentPosition` to the position passed as argument.

The :sip:ref:`~PyQt6.QtGui.QPainterPath.currentPosition` of the :sip:ref:`~PyQt6.QtGui.QPainterPath` object is always the end position of the last subpath that was added (or the initial start point). Use the :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo` function to move the :sip:ref:`~PyQt6.QtGui.QPainterPath.currentPosition` without adding a component. The :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo` function implicitly starts a new subpath, and closes the previous one. Another way of starting a new subpath is to call the :sip:ref:`~PyQt6.QtGui.QPainterPath.closeSubpath` function which closes the current path by adding a line from the :sip:ref:`~PyQt6.QtGui.QPainterPath.currentPosition` back to the path's start position. Note that the new path will have (0, 0) as its initial :sip:ref:`~PyQt6.QtGui.QPainterPath.currentPosition`.

:sip:ref:`~PyQt6.QtGui.QPainterPath` class also provides several convenience functions to add closed subpaths to a painter path: :sip:ref:`~PyQt6.QtGui.QPainterPath.addEllipse`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addPath`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addRect`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addRegion` and :sip:ref:`~PyQt6.QtGui.QPainterPath.addText`. The :sip:ref:`~PyQt6.QtGui.QPainterPath.addPolygon` function adds an *unclosed* subpath. In fact, these functions are all collections of :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo` and :sip:ref:`~PyQt6.QtGui.QPainterPath.cubicTo` operations.

In addition, a path can be added to the current path using the :sip:ref:`~PyQt6.QtGui.QPainterPath.connectPath` function. But note that this function will connect the last element of the current path to the first element of given one by adding a line.

Below is a code snippet that shows how a :sip:ref:`~PyQt6.QtGui.QPainterPath` object can be used:

+---------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-construction-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                       |     :lines: 75-88                                                                                       |
+---------------------------------------+---------------------------------------------------------------------------------------------------------+

The painter path is initially empty when constructed. We first add a rectangle, which is a closed subpath. Then we add two bezier curves which together form a closed subpath even though they are not closed individually. Finally we draw the entire path. The path is filled using the default fill rule, :sip:ref:`~PyQt6.QtCore.Qt.FillRule.OddEvenFill`. Qt provides two methods for filling paths:

+--------------------------------------------------+--------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.FillRule.OddEvenFill` | :sip:ref:`~PyQt6.QtCore.Qt.FillRule.WindingFill` |
+==================================================+==================================================+
| |image-qt-fillrule-oddeven-png|                  | |image-qt-fillrule-winding-png|                  |
+--------------------------------------------------+--------------------------------------------------+

See the :sip:ref:`~PyQt6.QtCore.Qt.FillRule` documentation for the definition of the rules. A painter path's currently set fill rule can be retrieved using the :sip:ref:`~PyQt6.QtGui.QPainterPath.fillRule` function, and altered using the :sip:ref:`~PyQt6.QtGui.QPainterPath.setFillRule` function.

.. _qpainterpath-qpainterpath-information:

QPainterPath Information
------------------------

The :sip:ref:`~PyQt6.QtGui.QPainterPath` class provides a collection of functions that returns information about the path and its elements.

The :sip:ref:`~PyQt6.QtGui.QPainterPath.currentPosition` function returns the end point of the last subpath that was added (or the initial start point). The :sip:ref:`~PyQt6.QtGui.QPainterPath.elementAt` function can be used to retrieve the various subpath elements, the *number* of elements can be retrieved using the :sip:ref:`~PyQt6.QtGui.QPainterPath.elementCount` function, and the :sip:ref:`~PyQt6.QtGui.QPainterPath.isEmpty` function tells whether this :sip:ref:`~PyQt6.QtGui.QPainterPath` object contains any elements at all.

The :sip:ref:`~PyQt6.QtGui.QPainterPath.controlPointRect` function returns the rectangle containing all the points and control points in this path. This function is significantly faster to compute than the exact :sip:ref:`~PyQt6.QtGui.QPainterPath.boundingRect` which returns the bounding rectangle of this painter path with floating point precision.

Finally, :sip:ref:`~PyQt6.QtGui.QPainterPath` provides the :sip:ref:`~PyQt6.QtGui.QPainterPath.contains` function which can be used to determine whether a given point or rectangle is inside the path, and the :sip:ref:`~PyQt6.QtGui.QPainterPath.intersects` function which determines if any of the points inside a given rectangle also are inside this path.

.. _qpainterpath-qpainterpath-conversion:

QPainterPath Conversion
-----------------------

For compatibility reasons, it might be required to simplify the representation of a painter path: :sip:ref:`~PyQt6.QtGui.QPainterPath` provides the :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon`, :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygons` and :sip:ref:`~PyQt6.QtGui.QPainterPath.toSubpathPolygons` functions which convert the painter path into a polygon. The :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon` returns the painter path as one single polygon, while the two latter functions return a list of polygons.

The :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygons` and :sip:ref:`~PyQt6.QtGui.QPainterPath.toSubpathPolygons` functions are provided because it is usually faster to draw several small polygons than to draw one large polygon, even though the total number of points drawn is the same. The difference between the two is the *number* of polygons they return: The :sip:ref:`~PyQt6.QtGui.QPainterPath.toSubpathPolygons` creates one polygon for each subpath regardless of intersecting subpaths (i.e. overlapping bounding rectangles), while the :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygons` functions creates only one polygon for overlapping subpaths.

The :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygon` and :sip:ref:`~PyQt6.QtGui.QPainterPath.toFillPolygons` functions first convert all the subpaths to polygons, then uses a rewinding technique to make sure that overlapping subpaths can be filled using the correct fill rule. Note that rewinding inserts additional lines in the polygon so the outline of the fill polygon does not match the outline of the path.

.. _qpainterpath-examples:

Examples
--------

Qt provides the Painter Paths Example and the Vector Deformation example which are located in Qt's example directory.

The Painter Paths Example shows how painter paths can be used to build complex shapes for rendering and lets the user experiment with the filling and stroking. The Vector Deformation Example shows how to use :sip:ref:`~PyQt6.QtGui.QPainterPath` to draw text.

+----------------------------------+-------------------------------+
| Painter Paths Example            | Vector Deformation Example    |
+==================================+===============================+
| |image-qpainterpath-example-png| | |image-qpainterpath-demo-png| |
+----------------------------------+-------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPathStroker`, :sip:ref:`~PyQt6.QtGui.QPainter`, :sip:ref:`~PyQt6.QtGui.QRegion`.

.. |image-qpainterpath-construction-png| image:: ../../../images/qpainterpath-construction.png
.. |image-qt-fillrule-oddeven-png| image:: ../../../images/qt-fillrule-oddeven.png
.. |image-qt-fillrule-winding-png| image:: ../../../images/qt-fillrule-winding.png
.. |image-qpainterpath-example-png| image:: ../../../images/qpainterpath-example.png
.. |image-qpainterpath-demo-png| image:: ../../../images/qpainterpath-demo.png
