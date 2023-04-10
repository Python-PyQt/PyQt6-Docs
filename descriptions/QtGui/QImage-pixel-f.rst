.. sip:method-description::
    :status: todo
    :pysig: b77dc1c2a27beac49df804498eb37df9
    :realsig: (const QPoint&) const
    :digest: 97765de18631d335a9ee0dfdf78b1191

Returns the color of the pixel at the given *position*.

If the *position* is not valid, the results are undefined.

**Warning:** This function is expensive when used for massive pixel manipulations. Use constBits() or constScanLine() when many pixels needs to be read.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setPixel`, :sip:ref:`~PyQt6.QtGui.QImage.valid`, Pixel Manipulation.
