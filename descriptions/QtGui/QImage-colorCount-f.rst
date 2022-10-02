.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 9964112fb01621e6aaada18f34468bbb

Returns the size of the color table for the image.

Notice that colorCount() returns 0 for 32-bpp images because these images do not use color tables, but instead encode pixel values as ARGB quadruplets.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setColorCount`, Image Information.
