.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 75d856f54091199644e56e4f21f896c2

Resizes the color table to contain *colorCount* entries.

If the color table is expanded, all the extra colors will be set to transparent (i.e :sip:ref:`~PyQt6.QtGui.qRgba`\ (0, 0, 0, 0)).

When the image is used, the color table must be large enough to have entries for all the pixel/index values present in the image, otherwise the results are undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.colorCount`, :sip:ref:`~PyQt6.QtGui.QImage.colorTable`, :sip:ref:`~PyQt6.QtGui.QImage.setColor`, Image Transformations.
