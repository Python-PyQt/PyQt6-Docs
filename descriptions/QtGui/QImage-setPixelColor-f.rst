.. sip:method-description::
    :status: todo
    :pysig: bfff83bf3dbc007b25204ffa798d1868
    :realsig: (const QPoint&, const QColor&)
    :digest: f8f39349c3eff4eccd8e70eab67806af

Sets the color at the given *position* to *color*.

If *position* is not a valid coordinate pair in the image, or the image's format is either monochrome or paletted, the result is undefined.

**Warning:** This function is expensive due to the call of the internal ``detach()`` function called within; if performance is a concern, we recommend the use of scanLine() or bits() to access pixel data directly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.pixelColor`, :sip:ref:`~PyQt6.QtGui.QImage.pixel`, Pixel Manipulation.
