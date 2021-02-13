.. sip:method-description::
    :status: todo
    :pysig: beba91dd4b7c0021937ae4c420312d80
    :realsig: (QImage::InvertMode)
    :digest: aac4885a29c9d486a8b252d595443b6d

Inverts all pixel values in the image.

The given invert *mode* only have a meaning when the image's depth is 32. The default *mode* is :sip:ref:`~PyQt6.QtGui.QImage.InvertMode.InvertRgb`, which leaves the alpha channel unchanged. If the *mode* is :sip:ref:`~PyQt6.QtGui.QImage.InvertMode.InvertRgba`, the alpha bits are also inverted.

Inverting an 8-bit image means to replace all pixels using color index *i* with a pixel using color index 255 minus *i*. The same is the case for a 1-bit image. Note that the color table is *not* changed.

If the image has a premultiplied alpha channel, the image is first converted to an unpremultiplied image format to be inverted and then converted back.

.. seealso:: Image Transformations.
