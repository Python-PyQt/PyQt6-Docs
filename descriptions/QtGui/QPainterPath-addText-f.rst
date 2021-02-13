.. sip:method-description::
    :status: todo
    :pysig: 9bb87e2dc4ddc1154a38e414892d3453
    :realsig: (const QPointF&,const QFont&,const QString&)
    :digest: 6b31fd4c9e17fa19d9dbc4c0122c7ecf

Adds the given *text* to this path as a set of closed subpaths created from the *font* supplied. The subpaths are positioned so that the left end of the text's baseline lies at the specified *point*.

+----------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-qpainterpath-addtext-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterpath.py |
|                                  |     :lines: 199-210                                                                                     |
+----------------------------------+---------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawText`, Composing a QPainterPath.

.. |image-qpainterpath-addtext-png| image:: ../../../images/qpainterpath-addtext.png
