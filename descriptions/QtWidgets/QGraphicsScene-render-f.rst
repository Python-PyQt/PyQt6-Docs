.. sip:method-description::
    :status: todo
    :pysig: 83b33bce1fe6e1874db5a88f4c0b5efb
    :realsig: (QPainter*,const QRectF&,const QRectF&,Qt::AspectRatioMode)
    :digest: ef063385b2cdd527a89ae83cba692905

Renders the *source* rect from scene into *target*, using *painter*. This function is useful for capturing the contents of the scene onto a paint device, such as a :sip:ref:`~PyQt6.QtGui.QImage` (e.g., to take a screenshot), or for printing with QPrinter. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsscene.py
    :lines: 63-70

If *source* is a null rect, this function will use :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.sceneRect` to determine what to render. If *target* is a null rect, the dimensions of *painter*'s paint device will be used.

The source rect contents will be transformed according to *aspectRatioMode* to fit into the target rect. By default, the aspect ratio is kept, and *source* is scaled to fit in *target*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.render`.
