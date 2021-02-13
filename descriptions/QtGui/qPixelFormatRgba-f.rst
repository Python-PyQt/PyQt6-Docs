.. sip:method-description::
    :status: todo
    :pysig: 23b02bbc10f3d04b7951445a7460e8dd
    :realsig: (uchar,uchar,uchar,uchar,QPixelFormat::AlphaUsage,QPixelFormat::AlphaPosition,QPixelFormat::AlphaPremultiplied,QPixelFormat::TypeInterpretation)
    :digest: 4c6aeb871ee67a953f4df0d3126f446b

Constructor function making an RGB pixelformat. *redSize* *greenSize* *blueSize* represent the size of each color channel. *alphaSize* describes the alpha channel size and its position is described with *alphaPosition*. *alphaUsage* is used to determine if the alpha channel is used or not. Setting the alpha channel size to 8 and alphaUsage to :sip:ref:`~PyQt6.QtGui.QPixelFormat.AlphaUsage.IgnoresAlpha` is how it is possible to create a 32 bit format where the rgb channels only use 24 bits combined. *premultiplied* *typeInterpretation* are accessible with accessors with the same name.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation`.
