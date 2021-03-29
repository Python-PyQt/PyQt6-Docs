.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: f8c60851351f1d781ba34521e2d6acf7

Sets the miter limit of the generated outlines to *limit*.

The miter limit describes how far from each join the miter join can extend. The limit is specified in units of the currently set width. So the pixelwise miter limit will be ``miterlimit \* width``.

This value is only used if the join style is :sip:ref:`~PyQt6.QtCore.Qt.PenJoinStyle.MiterJoin`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.miterLimit`.
