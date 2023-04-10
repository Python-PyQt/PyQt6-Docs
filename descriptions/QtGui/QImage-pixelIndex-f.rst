.. sip:method-description::
    :status: todo
    :pysig: b77dc1c2a27beac49df804498eb37df9
    :realsig: (const QPoint&) const
    :digest: 1e3c10d0a6360b1130eff12956be2323

Returns the pixel index at the given *position*.

If *position* is not valid, or if the image is not a paletted image (depth() > 8), the results are undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.valid`, Pixel Manipulation.
