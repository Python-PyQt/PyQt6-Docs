.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 74da19c995fca9d509a4d6345c2aef88

For image formats that support animation, this function returns the number of times the animation should loop. If this function returns -1, it can either mean the animation should loop forever, or that an error occurred. If an error occurred, :sip:ref:`~PyQt6.QtGui.QImageReader.canRead` will return false.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.supportsAnimation`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.loopCount`, :sip:ref:`~PyQt6.QtGui.QImageReader.canRead`.
