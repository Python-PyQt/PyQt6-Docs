.. sip:method-description::
    :status: todo
    :pysig: 359cf517e7cce924f18cbc82d0240ef5
    :realsig: (QPainter*,const QRectF&,const QRect&,Qt::AspectRatioMode)
    :digest: 8268ababfeb7cb9afeabf141b82e3162

Renders the *source* rect, which is in view coordinates, from the scene into *target*, which is in paint device coordinates, using *painter*. This function is useful for capturing the contents of the view onto a paint device, such as a :sip:ref:`~PyQt6.QtGui.QImage` (e.g., to take a screenshot), or for printing to QPrinter. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsview.py
    :lines: 90-112

If *source* is a null rect, this function will use viewport()->rect() to determine what to draw. If *target* is a null rect, the full dimensions of *painter*'s paint device (e.g., for a QPrinter, the page size) will be used.

The source rect contents will be transformed according to *aspectRatioMode* to fit into the target rect. By default, the aspect ratio is kept, and *source* is scaled to fit in *target*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.render`.
