.. sip:class-description::
    :status: todo
    :brief: Class for describing different pixel layouts in graphics buffers
    :digest: 9cd82e3c9a28b30a39f4c6f4b986d4ac

:sip:ref:`~PyQt6.QtGui.QPixelFormat` is a class for describing different pixel layouts in graphics buffers.

In Qt there is a often a need to represent the layout of the pixels in a graphics buffer. :sip:ref:`~PyQt6.QtGui.QPixelFormat` can describe up to 5 color channels and 1 alpha channel, including details about how these channels are represented in memory individually and in relation to each other.

The :sip:ref:`~PyQt6.QtGui.QPixelFormat.typeInterpretation` and :sip:ref:`~PyQt6.QtGui.QPixelFormat.byteOrder` determines how each pixel should be read/interpreted, while :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaSize`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaUsage`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaPosition`, and :sip:ref:`~PyQt6.QtGui.QPixelFormat.premultiplied` describes the position and properties of the possible alpha channel.

There is no support for describing YUV's macro pixels. Instead a list of :sip:ref:`~PyQt6.QtGui.QPixelFormat.YUVLayout` is provided. When a :sip:ref:`~PyQt6.QtGui.QPixelFormat` describes a YUV format, the :sip:ref:`~PyQt6.QtGui.QPixelFormat.bitsPerPixel` value is deduced from the YUV layout.
