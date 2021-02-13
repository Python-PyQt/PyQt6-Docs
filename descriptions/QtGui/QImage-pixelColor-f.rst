.. sip:method-description::
    :status: todo
    :pysig: 418b173bfdd0409b8080a03ae39dcb53
    :realsig: (const QPoint&) const
    :digest: 917b9ccb6bcee5c44f0c7e882a23ff88

Returns the color of the pixel at the given *position* as a :sip:ref:`~PyQt6.QtGui.QColor`.

If the *position* is not valid, an invalid :sip:ref:`~PyQt6.QtGui.QColor` is returned.

**Warning:** This function is expensive when used for massive pixel manipulations. Use :sip:ref:`~PyQt6.QtGui.QImage.constBits` or :sip:ref:`~PyQt6.QtGui.QImage.constScanLine` when many pixels needs to be read.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setPixelColor`, :sip:ref:`~PyQt6.QtGui.QImage.setPixel`, :sip:ref:`~PyQt6.QtGui.QImage.valid`, :sip:ref:`~PyQt6.QtGui.QImage.constBits`, :sip:ref:`~PyQt6.QtGui.QImage.constScanLine`, Pixel Manipulation.
