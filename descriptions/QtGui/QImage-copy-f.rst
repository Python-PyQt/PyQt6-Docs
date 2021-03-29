.. sip:method-description::
    :status: todo
    :pysig: f79cc74f3815102bd1d724a9c1fb1d97
    :realsig: (const QRect&) const
    :digest: 1669f96c2c6d36637383e3609d11fab2

Returns a sub-area of the image as a new image.

The returned image is copied from the position (\ *rectangle*.x(), *rectangle*.y()) in this image, and will always have the size of the given *rectangle*.

In areas beyond this image, pixels are set to 0. For 32-bit RGB images, this means black; for 32-bit ARGB images, this means transparent black; for 8-bit images, this means the color with index 0 in the color table which can be anything; for 1-bit images, this means :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color0`.

If the given *rectangle* is a null rectangle the entire image is copied.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage`.
