.. sip:enum-description::
    :status: todo
    :digest: de0551bcc558c22831adaf8b808c9c36

The following image formats are available in Qt. See the notes after the table.

Byte-ordered formats have a :sip:ref:`~PyQt6.QtGui.QPixelFormat.typeInterpretation` of :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedByte`, meaning the individual color components are stored in memory in a fixed order, e.g 0xRR, 0xGG, 0xBB, 0xAA, regardless of the endianness of the platform. These formats should be read as individual bytes, or interpreted as :sip:ref:`~PyQt6.QtGui.QPixelFormat.ByteOrder.BigEndian` if read in larger chunks.

**Note:** Drawing into a :sip:ref:`~PyQt6.QtGui.QImage` with format QImage::Format_Indexed8 or QImage::Format_CMYK8888 is not supported.

**Note:** Avoid most rendering directly to most of these formats using :sip:ref:`~PyQt6.QtGui.QPainter`. Rendering is best optimized to the ``Format_RGB32`` and ``Format_ARGB32_Premultiplied`` formats, and secondarily for rendering to the ``Format_RGB16``, ``Format_RGBX8888``, ``Format_RGBA8888_Premultiplied``, ``Format_RGBX64`` and ``Format_RGBA64_Premultiplied`` formats

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat`, :sip:ref:`~PyQt6.QtGui.QImage.format`.
