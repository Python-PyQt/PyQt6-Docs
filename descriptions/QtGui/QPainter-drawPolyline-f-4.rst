.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: (const QPointF*,int)
    :digest: 69d14674fd00789eaa4d7401f3c3d9ec

Draws the polyline defined by the first *pointCount* points in *points* using the current pen.

Note that unlike the :sip:ref:`~PyQt6.QtGui.QPainter.drawPolygon` function the last point is *not* connected to the first, neither is the polyline filled.

+-----------------------------------------------------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|     :lines: 263-270                                                                                 |
+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawLines`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPolygon`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.
