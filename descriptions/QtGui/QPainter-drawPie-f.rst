.. sip:method-description::
    :status: todo
    :pysig: 3465554a88c9f3336441cc762a92d046
    :realsig: (const QRectF&,int,int)
    :digest: 5a38ee24a333ca3338214363437ce892

Draws a pie defined by the given *rectangle*, *startAngle* and *spanAngle*.

The pie is filled with the current :sip:ref:`~PyQt6.QtGui.QPainter.brush`.

The startAngle and spanAngle must be specified in 1/16th of a degree, i.e. a full circle equals 5760 (16 \* 360). Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction. Zero degrees is at the 3 o'clock position.

+--------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-pie-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                          |     :lines: 234-239                                                                                 |
+--------------------------+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawEllipse`, :sip:ref:`~PyQt6.QtGui.QPainter.drawChord`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qpainter-pie-png| image:: ../../../images/qpainter-pie.png
