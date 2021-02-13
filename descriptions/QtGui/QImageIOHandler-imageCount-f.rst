.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: a33b09d98e7347b23e871e070a89a219

For image formats that support animation, this function returns the number of images in the animation. If the image format does not support animation, or if it is unable to determine the number of images, 0 is returned.

The default implementation returns 1 if :sip:ref:`~PyQt6.QtGui.QImageIOHandler.canRead` returns ``true``; otherwise 0 is returned.
