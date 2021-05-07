.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: d1f89b9fa655a15e85e390588b2ea193

Returns the color in the color table at index *i*. The first color is at index 0.

The colors in an image's color table are specified as ARGB quadruplets (QRgb). Use the , , , and  functions to get the color value components.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setColor`, :sip:ref:`~PyQt6.QtGui.QImage.pixelIndex`, Pixel Manipulation.
