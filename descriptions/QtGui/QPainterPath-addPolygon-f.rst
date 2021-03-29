.. sip:method-description::
    :status: todo
    :pysig: a378845a4ab49db069aa33c91dbcfa47
    :realsig: (const QPolygonF&)
    :digest: bd52d0ce01b86946aba217ed5a39fb22

Adds the given *polygon* to the path as an (unclosed) subpath.

Note that the current position after the polygon has been added, is the last point in *polygon*. To draw a line back to the first point, use the :sip:ref:`~PyQt6.QtGui.QPainterPath.closeSubpath` function.

+-------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-addpolygon-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                     |     :lines: 159-169                                                                                     |
+-------------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo`, Composing a QPainterPath.

.. |image-qpainterpath-addpolygon-png| image:: ../../../images/qpainterpath-addpolygon.png
