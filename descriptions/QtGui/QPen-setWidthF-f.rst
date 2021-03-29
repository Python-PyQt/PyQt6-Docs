.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: ef5bb9a186515f24e6afcc39b4436bea

Sets the pen width to the given *width* in pixels with floating point precision.

A line width of zero indicates a cosmetic pen. This means that the pen width is always drawn one pixel wide, independent of the transformation on the painter.

Setting a pen width with a negative value is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.setWidth`, :sip:ref:`~PyQt6.QtGui.QPen.widthF`.
