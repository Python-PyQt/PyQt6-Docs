.. sip:method-description::
    :status: todo
    :pysig: 9bb87e2dc4ddc1154a38e414892d3453
    :realsig: (const QPointF&,const QFont&,const QString&)
    :digest: da1c4c4d0b1c410a64640371c24a7888

Adds the given *text* to this path as a set of closed subpaths created from the *font* supplied. The subpaths are positioned so that the left end of the text's baseline lies at the specified *point*.

Some fonts may yield overlapping subpaths and will require the ``Qt::WindingFill`` fill rule for correct rendering.

+----------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-addtext-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                  |     :lines: 199-210                                                                                     |
+----------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawText`, Composing a QPainterPath, :sip:ref:`~PyQt6.QtGui.QPainterPath.setFillRule`.

.. |image-qpainterpath-addtext-png| image:: ../../../images/qpainterpath-addtext.png
