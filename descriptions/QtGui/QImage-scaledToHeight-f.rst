.. sip:method-description::
    :status: todo
    :pysig: d04bd697ee783814ff72a1caabfc1de8
    :realsig: (int,Qt::TransformationMode) const
    :digest: 558512eec7f043d89a8019d4fc39afc3

Returns a scaled copy of the image. The returned image is scaled to the given *height* using the specified transformation *mode*.

This function automatically calculates the width of the image so that the ratio of the image is preserved.

If the given *height* is 0 or negative, a null image is returned.

.. seealso:: Image Transformations.
