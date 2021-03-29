.. sip:method-description::
    :status: todo
    :pysig: 21e84a0b2fa3720786d69a4e169344e0
    :realsig: (const QTransform&,Qt::TransformationMode) const
    :digest: bffcf093e139c56939bfe18b8b68d23d

Returns a copy of the pixmap that is transformed using the given transformation *transform* and transformation *mode*. The original pixmap is not changed.

The transformation *transform* is internally adjusted to compensate for unwanted translation; i.e. the pixmap produced is the smallest pixmap that contains all the transformed points of the original pixmap. Use the :sip:ref:`~PyQt6.QtGui.QPixmap.trueMatrix` function to retrieve the actual matrix used for transforming the pixmap.

This function is slow because it involves transformation to a :sip:ref:`~PyQt6.QtGui.QImage`, non-trivial computations and a transformation back to a :sip:ref:`~PyQt6.QtGui.QPixmap`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.trueMatrix`, Pixmap Transformations.
