.. sip:method-description::
    :status: todo
    :pysig: e32e90e2d80163f671fe1fb98f891837
    :realsig: (uchar,uchar,QPixelFormat::AlphaUsage,QPixelFormat::AlphaPosition,QPixelFormat::TypeInterpretation)
    :digest: 48923f8c77d1b30e0a77a0224fcf37d3

Constructor function for creating HSV formats. The channel count will be 3 or 4 depending on if *alphaSize* is bigger than 0.

*channelSize* will set the hueSize saturationSize and brightnessSize to the same value.

*alphaUsage* *alphaPosition* and *typeInterpretation* are all accessible with the accessors with the same name.
