.. sip:method-description::
    :status: todo
    :pysig: a33121c659d5a40473fe749ec1958380
    :realsig: (const QPointF*,int,Qt::FillRule)
    :digest: e2ba2a465a271cab02b88e1a2d389bbf

Draws the polygon defined by the first *pointCount* points in the array *points* using the current pen and brush.

+------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-polygon-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                              |     :lines: 278-286                                                                                 |
+------------------------------+-----------------------------------------------------------------------------------------------------+

The first point is implicitly connected to the last point, and the polygon is filled with the current :sip:ref:`~PyQt6.QtGui.QPainter.brush`.

If *fillRule* is :sip:ref:`~PyQt6.QtCore.Qt.FillRule.WindingFill`, the polygon is filled using the winding fill algorithm. If *fillRule* is :sip:ref:`~PyQt6.QtCore.Qt.FillRule.OddEvenFill`, the polygon is filled using the odd-even fill algorithm. See :sip:ref:`~PyQt6.QtCore.Qt.FillRule` for a more detailed description of these fill rules.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawConvexPolygon`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPolyline`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qpainter-polygon-png| image:: ../../../images/qpainter-polygon.png
