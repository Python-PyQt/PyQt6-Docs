.. sip:method-description::
    :status: todo
    :pysig: b5f637b83de183876dea2bb16cd46020
    :realsig: (const QRectF&,qreal,qreal)
    :digest: c870d9d876aaa1673d326a26d870cf08

Creates an arc that occupies the given *rectangle*, beginning at the specified *startAngle* and extending *sweepLength* degrees counter-clockwise.

Angles are specified in degrees. Clockwise arcs can be specified using negative angles.

Note that this function connects the starting point of the arc to the current position if they are not already connected. After the arc has been added, the current position is the last point in arc. To draw a line back to the first point, use the :sip:ref:`~PyQt6.QtGui.QPainterPath.closeSubpath` function.

+--------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-arcto-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                |     :lines: 123-131                                                                                     |
+--------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.arcMoveTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addEllipse`, :sip:ref:`~PyQt6.QtGui.QPainter.drawArc`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPie`, Composing a QPainterPath.

.. |image-qpainterpath-arcto-png| image:: ../../../images/qpainterpath-arcto.png
