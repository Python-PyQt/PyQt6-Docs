.. sip:method-description::
    :status: todo
    :pysig: 122873e1820526b1215655200c94740f
    :realsig: (const QPoint&,const QColor&)
    :digest: 6a8065b37a6657bcca9aa75500cf2209

Sets the color at the given *position* to *color*.

If *position* is not a valid coordinate pair in the image, or the image's format is either monochrome or paletted, the result is undefined.

**Warning:** This function is expensive due to the call of the internal ``detach()`` function called within; if performance is a concern, we recommend the use of scanLine() or bits() to access pixel data directly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.pixel`, Pixel Manipulation.
