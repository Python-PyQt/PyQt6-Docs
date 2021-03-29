.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: (const QImage&)
    :digest: 833d566221fa115ece009caf02e195d5

Sets the alpha channel of this image to the given *alphaChannel*.

If *alphaChannel* is an 8 bit alpha image, the alpha values are used directly. Otherwise, *alphaChannel* is converted to 8 bit grayscale and the intensity of the pixel values is used.

If the image already has an alpha channel, the existing alpha channel is multiplied with the new one. If the image doesn't have an alpha channel it will be converted to a format that does.

The operation is similar to painting *alphaChannel* as an alpha image over this image using ``QPainter::CompositionMode_DestinationIn``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.hasAlphaChannel`, Image Transformations, Image Formats.
