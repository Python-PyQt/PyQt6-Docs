.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: (const QRectF&)
    :digest: 9cf01c3bf0f0fde4a4ab14487eca5a2f

Creates an ellipse within the specified *boundingRectangle* and adds it to the painter path as a closed subpath.

The ellipse is composed of a clockwise curve, starting and finishing at zero degrees (the 3 o'clock position).

+-------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-addellipse-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                     |     :lines: 178-188                                                                                     |
+-------------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.arcTo`, :sip:ref:`~PyQt6.QtGui.QPainter.drawEllipse`, Composing a QPainterPath.

.. |image-qpainterpath-addellipse-png| image:: ../../../images/qpainterpath-addellipse.png
