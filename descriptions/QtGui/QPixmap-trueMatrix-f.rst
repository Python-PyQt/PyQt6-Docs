.. sip:method-description::
    :status: todo
    :pysig: 58947aa48eef70bd58e1fa6ed28fb71e
    :realsig: (const QTransform&,int,int)
    :digest: 91ac17c8edc92b9302b2f519e5320018

Returns the actual matrix used for transforming a pixmap with the given *width*, *height* and *matrix*.

When transforming a pixmap using the transformed() function, the transformation matrix is internally adjusted to compensate for unwanted translation, i.e. transformed() returns the smallest pixmap containing all transformed points of the original pixmap. This function returns the modified matrix, which maps points correctly from the original pixmap into the new pixmap.

.. seealso:: Pixmap Transformations, :sip:ref:`~PyQt6.QtGui.QPixmap.transformed`.
