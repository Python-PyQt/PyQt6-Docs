.. sip:method-description::
    :status: todo
    :pysig: 3465554a88c9f3336441cc762a92d046
    :realsig: (const QRectF&,int,int)
    :digest: 8457dfb92fd60a117cb6a40045136884

Draws the chord defined by the given *rectangle*, *startAngle* and *spanAngle*. The chord is filled with the current :sip:ref:`~PyQt6.QtGui.QPainter.brush`.

The startAngle and spanAngle must be specified in 1/16th of a degree, i.e. a full circle equals 5760 (16 \* 360). Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction. Zero degrees is at the 3 o'clock position.

+----------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-chord-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                            |     :lines: 249-254                                                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawArc`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPie`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qpainter-chord-png| image:: ../../../images/qpainter-chord.png
