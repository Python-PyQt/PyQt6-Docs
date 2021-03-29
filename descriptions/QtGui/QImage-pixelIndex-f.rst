.. sip:method-description::
    :status: todo
    :pysig: b77dc1c2a27beac49df804498eb37df9
    :realsig: (const QPoint&) const
    :digest: f985945ab0d9cabfe4140e387d7d33bf

Returns the pixel index at the given *position*.

If *position* is not valid, or if the image is not a paletted image (\ :sip:ref:`~PyQt6.QtGui.QImage.depth` > 8), the results are undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.valid`, :sip:ref:`~PyQt6.QtGui.QImage.depth`, Pixel Manipulation.
