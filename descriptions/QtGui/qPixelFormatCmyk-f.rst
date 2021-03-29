.. sip:method-description::
    :status: todo
    :pysig: 90fd772ec78b2b1f3d034cca65e2d5b3
    :realsig: (uchar,uchar,QPixelFormat::AlphaUsage,QPixelFormat::AlphaPosition,QPixelFormat::TypeInterpretation)
    :digest: cc4f10be0e68fd4b26c5654a20f8986a

Constructor function for creating CMYK formats. The channel count will be 4 or 5 depending on if *alphaSize* is bigger than zero or not. The CMYK color channels will all be set to the value of *channelSize*.

*alphaUsage* *alphaPosition* and *typeInterpretation* are all accessible with the accessors with the same name.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation`.
