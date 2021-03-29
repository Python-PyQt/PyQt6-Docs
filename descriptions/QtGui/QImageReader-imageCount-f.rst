.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: d9fa2de3beb9ce90ccbf2eccadf54ee7

For image formats that support animation, this function returns the total number of images in the animation. If the format does not support animation, 0 is returned.

This function returns -1 if an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.supportsAnimation`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.imageCount`, :sip:ref:`~PyQt6.QtGui.QImageReader.canRead`.
