.. sip:method-description::
    :status: todo
    :pysig: 58947aa48eef70bd58e1fa6ed28fb71e
    :realsig: (const QTransform&,int,int)
    :digest: c2d1ec1365686970cf5195f8f3db45e6

Returns the actual matrix used for transforming an image with the given *width*, *height* and *matrix*.

When transforming an image using the :sip:ref:`~PyQt6.QtGui.QImage.transformed` function, the transformation matrix is internally adjusted to compensate for unwanted translation, i.e. :sip:ref:`~PyQt6.QtGui.QImage.transformed` returns the smallest image containing all transformed points of the original image. This function returns the modified matrix, which maps points correctly from the original image into the new image.

Unlike the other overload, this function creates transformation matrices that can be used to perform perspective transformations on images.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.transformed`, Image Transformations.
