.. sip:method-description::
    :status: todo
    :pysig: 1d557afd38e9b10837d8f94f0b85c942
    :realsig: (int)
    :digest: 9d463813c99bde01be1b82797af7e2de

Returns a pointer to the pixel data at the scanline with index *i*. The first scanline is at index 0.

The scanline data is as minimum 32-bit aligned. For 64-bit formats it follows the native alignment of 64-bit integers (64-bit for most platforms, but notably 32-bit on i386).

For example, to remove the green component of each pixel in an image:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimage.py
    :lines: 106-112

**Warning:** If you are accessing 32-bpp image data, cast the returned pointer to ``QRgb\*`` (QRgb has a 32-bit size) and use it to read/write the pixel value. You cannot use the ``uchar\*`` pointer directly, because the pixel format depends on the byte order on the underlying platform. Use , , , and  to access the pixels.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.bytesPerLine`, :sip:ref:`~PyQt6.QtGui.QImage.bits`, Pixel Manipulation, :sip:ref:`~PyQt6.QtGui.QImage.constScanLine`.
