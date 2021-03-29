.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: (const QRectF&)
    :digest: 3b734c0aaec1f2d6c9d0b88ffc94d01f

Draws the current *rectangle* with the current pen and brush.

A filled rectangle has a size of *rectangle*.size(). A stroked rectangle has a size of *rectangle*.size() plus the pen width.

+--------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-rectangle-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                                |     :lines: 184-187                                                                                 |
+--------------------------------+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawRects`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPolygon`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qpainter-rectangle-png| image:: ../../../images/qpainter-rectangle.png
