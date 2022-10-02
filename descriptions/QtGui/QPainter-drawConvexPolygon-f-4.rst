.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: (const QPointF*,int)
    :digest: 7a3d0211980f64be7bc2533ca9cc9690

Draws the convex polygon defined by the first *pointCount* points in the array *points* using the current pen.

+------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-polygon-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                              |     :lines: 295-303                                                                                 |
+------------------------------+-----------------------------------------------------------------------------------------------------+

The first point is implicitly connected to the last point, and the polygon is filled with the current :sip:ref:`~PyQt6.QtGui.QPainter.brush`. If the supplied polygon is not convex, i.e. it contains at least one angle larger than 180 degrees, the results are undefined.

On some platforms (e.g. X11), the drawConvexPolygon() function can be faster than the :sip:ref:`~PyQt6.QtGui.QPainter.drawPolygon` function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPolygon`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPolyline`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qpainter-polygon-png| image:: ../../../images/qpainter-polygon.png
