.. sip:method-description::
    :status: todo
    :pysig: 8a051ccafecbd6a31d148c731aa39add
    :realsig: (int,Qt::TransformationMode) const
    :digest: 6d4b057659ca28fcbbc9edf674a0fbc8

Returns a scaled copy of the image. The returned image is scaled to the given *height* using the specified transformation *mode*. The width of the pixmap is automatically calculated so that the aspect ratio of the pixmap is preserved.

If *height* is 0 or negative, a null pixmap is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.isNull`, Pixmap Transformations.
