.. sip:method-description::
    :status: todo
    :pysig: 32603454d4f10fa678787c4571fc43de
    :realsig: (const QPointF&,const QPointF&,const QPointF&)
    :digest: 6fdc3516c6c0e503152d829ad8b981bf

Adds a cubic Bezier curve between the current position and the given *endPoint* using the control points specified by *c1*, and *c2*.

After the curve is added, the current position is updated to be at the end point of the curve.

+----------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-cubicto-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                  |     :lines: 100-109                                                                                     |
+----------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.quadTo`, Composing a QPainterPath.

.. |image-qpainterpath-cubicto-png| image:: ../../../images/qpainterpath-cubicto.png
