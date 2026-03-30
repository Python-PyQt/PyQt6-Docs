.. sip:method-description::
    :status: todo
    :pysig: 87e8bbbf4286f5101770880115806e0d
    :realsig: () const
    :digest: 17317f19687081d7a28715e6dcc656ac

The type interpretation determines how each pixel should be read.

Each pixel is represented as one or more units of the given type, laid out sequentially in memory.

**Note:** The :sip:ref:`~PyQt6.QtGui.QPixelFormat.byteOrder` of the pixel format and the endianness of the host system only affect the memory layout of each individual unit being read — *not* the relative ordering of the units.

For example, :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono` has a :sip:ref:`~PyQt6.QtGui.QImage.pixelFormat` of 1 bits per pixel and a :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedByte` type interpretation, which should be read as a single ``byte``. Similarly, :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB888` has a :sip:ref:`~PyQt6.QtGui.QImage.pixelFormat` of 24 bits per pixel, and and a :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedByte` type interpretation, which should be read as three consecutive ``byte``\ s.

Many of the :sip:ref:`~PyQt6.QtGui.QImage` :sip:ref:`~PyQt6.QtGui.QImage.Format` are 32-bit with a type interpretation of :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedInteger`, which should be read as a single ``unsigned int``.

For :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.FloatingPoint` formats like :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGBA16FPx4` or :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGBA32FPx4` the type is determined based on the size of the individual color/alpha channels, with ``qfloat16`` for 16-bit half-float formats and ``float`` for 32-bit full-float formats.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.byteOrder`.
