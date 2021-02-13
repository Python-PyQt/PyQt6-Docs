.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 2026965ffe4c12ba7cc57ddb46872c90

For image formats that support animation, this function returns the number of milliseconds to wait until displaying the next frame in the animation. If the image format doesn't support animation, 0 is returned.

This function returns -1 if an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.supportsAnimation`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.nextImageDelay`, :sip:ref:`~PyQt6.QtGui.QImageReader.canRead`.
