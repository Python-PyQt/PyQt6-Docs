.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 699844044174676fefdc450004c2e96e

For image formats that support animation, this function steps over the current image, returning true if successful or false if there is no following image in the animation.

The default implementation calls :sip:ref:`~PyQt6.QtGui.QImageReader.read`, then discards the resulting image, but the image handler may have a more efficient way of implementing this operation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.jumpToImage`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.jumpToNextImage`.
