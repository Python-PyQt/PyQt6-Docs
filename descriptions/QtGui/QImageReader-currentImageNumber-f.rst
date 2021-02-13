.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b9c2117dfa52e639e6e690789647cf79

For image formats that support animation, this function returns the sequence number of the current frame. If the image format doesn't support animation, 0 is returned.

This function returns -1 if an error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.supportsAnimation`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.currentImageNumber`, :sip:ref:`~PyQt6.QtGui.QImageReader.canRead`.
