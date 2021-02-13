.. sip:method-description::
    :status: todo
    :pysig: 8a051ccafecbd6a31d148c731aa39add
    :realsig: (int,Qt::TransformationMode) const
    :digest: 3ec78f02caa6c149edd986aa081222ee

Returns a scaled copy of the image. The returned image is scaled to the given *width* using the specified transformation *mode*. The height of the pixmap is automatically calculated so that the aspect ratio of the pixmap is preserved.

If *width* is 0 or negative, a null pixmap is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.isNull`, Pixmap Transformations.
