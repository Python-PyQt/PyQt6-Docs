.. sip:method-description::
    :status: todo
    :pysig: d6a4c94553eea92c5a50744582dbc7cf
    :realsig: (QImage::Format)
    :digest: 206812e3b356b3de82cee68351789bd4

Changes the format of the image to *format* without changing the data. Only works between formats of the same depth.

Returns ``true`` if successful.

This function can be used to change images with alpha-channels to their corresponding opaque formats if the data is known to be opaque-only, or to change the format of a given image buffer before overwriting it with new data.

**Warning:** The function does not check if the image data is valid in the new format and will still return ``true`` if the depths are compatible. Operations on an image with invalid data are undefined.

**Warning:** If the image is not detached, this will cause the data to be copied.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.hasAlphaChannel`, :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat`.
