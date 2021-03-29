.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: (const QRectF&)
    :digest: e8fa55ca5337e9f75660f248ff0999bb

Draws the ellipse defined by the given *rectangle*.

A filled ellipse has a size of *rectangle*.\ :sip:ref:`~PyQt6.QtCore.QRect.size`. A stroked ellipse has a size of *rectangle*.\ :sip:ref:`~PyQt6.QtCore.QRect.size` plus the pen width.

+------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-ellipse-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                              |     :lines: 208-211                                                                                 |
+------------------------------+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPie`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qpainter-ellipse-png| image:: ../../../images/qpainter-ellipse.png
