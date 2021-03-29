.. sip:method-description::
    :status: todo
    :pysig: 927e7c6629190b12dfc98cd47ea847e4
    :realsig: (QPixelFormat::YUVLayout,uchar,QPixelFormat::AlphaUsage,QPixelFormat::AlphaPosition,QPixelFormat::AlphaPremultiplied,QPixelFormat::TypeInterpretation,QPixelFormat::ByteOrder)
    :digest: 81c3379f6fe1a5ee682798656f798844

Constructor function for creating a :sip:ref:`~PyQt6.QtGui.QPixelFormat` describing a YUV format with *yuvLayout*. *alphaSize* describes the size of a potential alpha channel and is position is described with *alphaPosition*. The "first" "second" .. "fifth" channels are all set to 0. *alphaUsage* *premultiplied* *typeInterpretation* and *byteOrder* will work as with other formats.
