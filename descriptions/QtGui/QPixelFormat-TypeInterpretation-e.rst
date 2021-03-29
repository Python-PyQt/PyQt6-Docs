.. sip:enum-description::
    :status: todo
    :digest: ad75f200f86f6088343f2e212b6980c8

This enum describes how each pixel is interpreted. If a pixel is read as a full 32 bit unsigned integer and then each channel is masked out, or if each byte is read as unsigned char values. Typically :sip:ref:`~PyQt6.QtGui.QImage` formats interpret one pixel as an unsigned integer and then the color channels are masked out. OpenGL on the other hand typically interpreted pixels "one byte after the other", Ie. unsigned byte.

:sip:ref:`~PyQt6.QtGui.QImage` also have the format Format_RGBA8888 (and its derivatives), where the pixels are interpreted as unsigned bytes. OpenGL has extensions that makes it possible to upload pixel buffers in an unsigned integer format.

.. image:: ../../../images/qpixelformat-argb32buffer.png

The image above shows a ARGB pixel in memory read as an unsigned integer. However, if this pixel was read byte for byte on a little endian system the first byte would be the byte containing the B-channel. The next byte would be the G-channel, then the R-channel and finally the A-channel. This shows that on little endian systems, how each pixel is interpreted is significant for integer formats. This is not the case on big endian systems.
