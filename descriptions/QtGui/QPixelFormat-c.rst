.. sip:class-description::
    :status: todo
    :brief: Class for describing different pixel layouts in graphics buffers
    :digest: 17660edcdee3e4d95402cabc6e7c967f

:sip:ref:`~PyQt6.QtGui.QPixelFormat` is a class for describing different pixel layouts in graphics buffers.

In Qt there is a often a need to represent the layout of the pixels in a graphics buffer. Internally :sip:ref:`~PyQt6.QtGui.QPixelFormat` stores everything in a 64 bit datastructure. This gives performance but also some limitations.

:sip:ref:`~PyQt6.QtGui.QPixelFormat` can describe 5 color channels and 1 alpha channel, each can use 6 bits to describe the size of the color channel.

The position of the alpha channel is described with a separate enum. This is to make it possible to describe :sip:ref:`~PyQt6.QtGui.QImage` formats like ARGB32, and also describe typical OpenGL formats like RBGA8888.

How pixels are suppose to be read is determined by the :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.TypeInterpretation` enum. It describes if color values are suppose to be read byte per byte, or if a pixel is suppose to be read as a complete int and then masked.

There is no support for describing YUV's macro pixels. Instead a list of YUV formats has been made. When a :sip:ref:`~PyQt6.QtGui.QPixelFormat` is describing a YUV format, the :sip:ref:`~PyQt6.QtGui.QPixelFormat.bitsPerPixel` value has been deduced by the YUV Layout enum. Also, the color channels should all be set to zero except the fifth color channel that should store the :sip:ref:`~PyQt6.QtGui.QPixelFormat.bitsPerPixel` value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.TypeInterpretation`.
