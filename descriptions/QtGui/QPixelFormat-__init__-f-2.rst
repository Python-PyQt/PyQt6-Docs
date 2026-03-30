.. sip:method-description::
    :status: todo
    :pysig: f16ab654c6d607e5b3b7df743f65d039
    :realsig: (QPixelFormat::ColorModel,uchar,uchar,uchar,uchar,uchar,uchar,QPixelFormat::AlphaUsage,QPixelFormat::AlphaPosition,QPixelFormat::AlphaPremultiplied,QPixelFormat::TypeInterpretation,QPixelFormat::ByteOrder,uchar)
    :digest: 5f8f3541608ae1246b1d6b8a289ed853

Creates a :sip:ref:`~PyQt6.QtGui.QPixelFormat` which assigns its data to the attributes. *colorModel* will be put into a buffer which is 4 bits long.

*firstSize* *secondSize* *thirdSize* *fourthSize* *fifthSize* *alphaSize* are all meant to represent the size of a channel. The channels will be used for different uses dependent on the *colorModel*. For RGB the firstSize will represent the Red channel. On CMYK it will represent the value of the Cyan channel.

*alphaUsage* represents if the alpha channel is used or not.

*alphaPosition* is the position of the alpha channel.

*premultiplied* represents if the alpha channel is already multiplied with the color channels.

*typeInterpretation* is how the pixel is interpreted.

*byteOrder* represents the endianness of the pixelformat. This defaults to :sip:ref:`~PyQt6.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian`, which will be resolve to the system's endianness for non-byte-ordered formats, and :sip:ref:`~PyQt6.QtGui.QPixelFormat.ByteOrder.BigEndian` for :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedByte`.

*subEnum* is used for colorModels that have to store some extra information with supplying an extra enum. This is used by YUV to store the YUV type The default value is 0.

**Note:** BGR formats have their own color model, and should not be described by using the opposite endianness of an RGB format.
