.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: (const QRectF&)
    :digest: 231273b16de6762d89911c7c90d68b7d

Adds the given *rectangle* to this path as a closed subpath.

The *rectangle* is added as a clockwise set of lines. The painter path's current position after the *rectangle* has been added is at the top-left corner of the rectangle.

+---------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-addrectangle-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                       |     :lines: 140-150                                                                                     |
+---------------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.addRegion`, :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo`, Composing a QPainterPath.

.. |image-qpainterpath-addrectangle-png| image:: ../../../images/qpainterpath-addrectangle.png
