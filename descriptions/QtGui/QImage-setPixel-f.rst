.. sip:method-description::
    :status: todo
    :pysig: b77dc1c2a27beac49df804498eb37df9
    :realsig: (const QPoint&,uint)
    :digest: e19828ccdad954d086168e7c58614881

Sets the pixel index or color at the given *position* to *index_or_rgb*.

If the image's format is either monochrome or paletted, the given *index_or_rgb* value must be an index in the image's color table, otherwise the parameter must be a QRgb value.

If *position* is not a valid coordinate pair in the image, or if *index_or_rgb* >= :sip:ref:`~PyQt6.QtGui.QImage.colorCount` in the case of monochrome and paletted images, the result is undefined.

**Warning:** This function is expensive due to the call of the internal ``detach()`` function called within; if performance is a concern, we recommend the use of scanLine() or bits() to access pixel data directly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.pixel`, Pixel Manipulation.
