.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: de5409504c77d63de318094fb2cd678e

Sets the pen width to the given *width* in pixels with integer precision.

A line width of zero indicates a cosmetic pen. This means that the pen width is always drawn one pixel wide, independent of the transformation set on the painter.

Setting a pen width with a negative value is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.setWidthF`, :sip:ref:`~PyQt6.QtGui.QPen.width`.
