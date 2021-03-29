.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (uint)
    :digest: 8baafe39940dda186acf69c95866aaeb

Fills the entire image with the given *pixelValue*.

If the depth of this image is 1, only the lowest bit is used. If you say fill(0), fill(2), etc., the image is filled with 0s. If you say fill(1), fill(3), etc., the image is filled with 1s. If the depth is 8, the lowest 8 bits are used and if the depth is 16 the lowest 16 bits are used.

Note: :sip:ref:`~PyQt6.QtGui.QImage.pixel` returns the color of the pixel at the given coordinates while QColor::pixel() returns the pixel value of the underlying window system (essentially an index value), so normally you will want to use :sip:ref:`~PyQt6.QtGui.QImage.pixel` to use a color from an existing image or :sip:ref:`~PyQt6.QtGui.QColor.rgb` to use a specific color.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.depth`, Image Transformations.
