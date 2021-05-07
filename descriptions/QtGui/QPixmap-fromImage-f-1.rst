.. sip:method-description::
    :status: todo
    :pysig: 4b2aaee167d6dc064d95916138d6a94d
    :realsig: (const QImage&,Qt::ImageConversionFlags)
    :digest: 0cda982ecf56cfa5d6a31a39ce159bbc

Converts the given *image* to a pixmap using the specified *flags* to control the conversion. The *flags* argument is a bitwise-OR of the Qt::ImageConversionFlags. Passing 0 for *flags* sets all the default options.

In case of monochrome and 8-bit images, the image is first converted to a 32-bit pixmap and then filled with the colors in the color table. If this is too expensive an operation, you can use :sip:ref:`~PyQt6.QtGui.QBitmap.fromImage` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.fromImageReader`, :sip:ref:`~PyQt6.QtGui.QPixmap.toImage`, Pixmap Conversion.
