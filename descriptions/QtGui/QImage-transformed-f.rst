.. sip:method-description::
    :status: todo
    :pysig: 2ac84508839a1c90beca853cdca612e3
    :realsig: (const QTransform&,Qt::TransformationMode) const
    :digest: 7b52bb679e94386eb2b9d98650168f61

Returns a copy of the image that is transformed using the given transformation *matrix* and transformation *mode*.

The returned image will normally have the same {Image Formats}{format} as the original image. However, a complex transformation may result in an image where not all pixels are covered by the transformed pixels of the original image. In such cases, those background pixels will be assigned a transparent color value, and the transformed image will be given a format with an alpha channel, even if the original image did not have that.

The transformation *matrix* is internally adjusted to compensate for unwanted translation; i.e. the image produced is the smallest image that contains all the transformed points of the original image. Use the :sip:ref:`~PyQt6.QtGui.QImage.trueMatrix` function to retrieve the actual matrix used for transforming an image.

Unlike the other overload, this function can be used to perform perspective transformations on images.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.trueMatrix`, Image Transformations.
