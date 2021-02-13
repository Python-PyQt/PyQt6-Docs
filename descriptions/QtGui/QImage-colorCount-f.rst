.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 72028d178996b8c668272de0a9915123

Returns the size of the color table for the image.

Notice that  returns 0 for 32-bpp images because these images do not use color tables, but instead encode pixel values as ARGB quadruplets.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setColorCount`, Image Information.
