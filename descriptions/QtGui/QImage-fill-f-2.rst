.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (uint)
    :digest: 1cb0635ed76b13e57ffe2c9e1ed923c5

Fills the entire image with the given *pixelValue*.

If the depth of this image is 1, only the lowest bit is used. If you say fill(0), fill(2), etc., the image is filled with 0s. If you say fill(1), fill(3), etc., the image is filled with 1s. If the depth is 8, the lowest 8 bits are used and if the depth is 16 the lowest 16 bits are used.

If the image depth is higher than 32bit the result is undefined.

**Note:** There are no corresponding value getter, though :sip:ref:`~PyQt6.QtGui.QImage.pixelIndex` will return the same value for indexed formats, and :sip:ref:`~PyQt6.QtGui.QImage.pixel` for RGB32, ARGB32, and ARGB32PM formats.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.depth`, Image Transformations.
