.. sip:method-description::
    :status: todo
    :pysig: 418b173bfdd0409b8080a03ae39dcb53
    :realsig: (const QPoint&) const
    :digest: 52588f7137d54db74d590e9f35bacdb2

Returns the color of the pixel at the given *position* as a :sip:ref:`~PyQt6.QtGui.QColor`.

If the *position* is not valid, an invalid :sip:ref:`~PyQt6.QtGui.QColor` is returned.

**Warning:** This function is expensive when used for massive pixel manipulations. Use constBits() or constScanLine() when many pixels needs to be read.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setPixel`, :sip:ref:`~PyQt6.QtGui.QImage.valid`, Pixel Manipulation.
