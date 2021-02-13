.. sip:method-description::
    :status: todo
    :pysig: 42bc621440f2bdcd8c3592b238ca23b1
    :realsig: (Qt::ImageConversionFlags) const
    :digest: a6a7dbe0bbc287198f2c40d66d51d4a8

Builds and returns a 1-bpp mask from the alpha buffer in this image. Returns a null image if the image's format is :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32`.

The *flags* argument is a bitwise-OR of the Qt::ImageConversionFlags, and controls the conversion process. Passing 0 for flags sets all the default options.

The returned image has little-endian bit order (i.e. the image's format is :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_MonoLSB`), which you can convert to big-endian (\ :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono`) using the :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat` function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.createHeuristicMask`, Image Transformations.
