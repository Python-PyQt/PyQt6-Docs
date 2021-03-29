.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 6a59ebf03ce39ac926f38ce2d70af204

For image formats that support animation, this function returns the sequence number of the current image in the animation. If this function is called before any image is :sip:ref:`~PyQt6.QtGui.QImageIOHandler.read`, -1 is returned. The number of the first image in the sequence is 0.

If the image format does not support animation, 0 is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageIOHandler.read`.
