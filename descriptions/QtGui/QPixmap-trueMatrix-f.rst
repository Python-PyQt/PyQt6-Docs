.. sip:method-description::
    :status: todo
    :pysig: 58947aa48eef70bd58e1fa6ed28fb71e
    :realsig: (const QTransform&,int,int)
    :digest: c594ce9277849e29e367c1a2278e4d0d

Returns the actual matrix used for transforming a pixmap with the given *width*, *height* and *matrix*.

When transforming a pixmap using the :sip:ref:`~PyQt6.QtGui.QPixmap.transformed` function, the transformation matrix is internally adjusted to compensate for unwanted translation, i.e. :sip:ref:`~PyQt6.QtGui.QPixmap.transformed` returns the smallest pixmap containing all transformed points of the original pixmap. This function returns the modified matrix, which maps points correctly from the original pixmap into the new pixmap.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.transformed`, Pixmap Transformations.
