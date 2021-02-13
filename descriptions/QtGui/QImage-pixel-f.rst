.. sip:method-description::
    :status: todo
    :pysig: b77dc1c2a27beac49df804498eb37df9
    :realsig: (const QPoint&) const
    :digest: 35c63c01a79949a8ffcb3b69b2f4b931

Returns the color of the pixel at the given *position*.

If the *position* is not valid, the results are undefined.

**Warning:** This function is expensive when used for massive pixel manipulations. Use :sip:ref:`~PyQt6.QtGui.QImage.constBits` or :sip:ref:`~PyQt6.QtGui.QImage.constScanLine` when many pixels needs to be read.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setPixel`, :sip:ref:`~PyQt6.QtGui.QImage.valid`, :sip:ref:`~PyQt6.QtGui.QImage.constBits`, :sip:ref:`~PyQt6.QtGui.QImage.constScanLine`, Pixel Manipulation.
