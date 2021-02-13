.. sip:method-description::
    :status: todo
    :pysig: d04bd697ee783814ff72a1caabfc1de8
    :realsig: (int,Qt::TransformationMode) const
    :digest: 2f1a01267bb31ce3b2cbc07994fed8ea

Returns a scaled copy of the image. The returned image is scaled to the given *width* using the specified transformation *mode*.

This function automatically calculates the height of the image so that its aspect ratio is preserved.

If the given *width* is 0 or negative, a null image is returned.

.. seealso:: Image Transformations.
