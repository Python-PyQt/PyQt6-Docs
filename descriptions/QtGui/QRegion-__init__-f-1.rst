.. sip:method-description::
    :status: todo
    :pysig: f7dba2c0411c0ef6af4394e6fc1d3906
    :realsig: (const QBitmap&)
    :digest: c43c4c84615216555ba32d995a7f5148

Constructs a region from the bitmap *bm*.

The resulting region consists of the pixels in bitmap *bm* that are :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color1`, as if each pixel was a 1 by 1 rectangle.

This constructor may create complex regions that will slow down painting when used. Note that drawing masked pixmaps can be done much faster using :sip:ref:`~PyQt6.QtGui.QPixmap.setMask`.
