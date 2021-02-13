.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: 0f47055d4a5ccd9f513013dae52dc0dc

Returns the color in the color table at index *i*. The first color is at index 0.

The colors in an image's color table are specified as ARGB quadruplets (QRgb). Use the :sip:ref:`~PyQt6.QtGui.qAlpha`, :sip:ref:`~PyQt6.QtGui.qRed`, :sip:ref:`~PyQt6.QtGui.qGreen`, and :sip:ref:`~PyQt6.QtGui.qBlue` functions to get the color value components.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setColor`, :sip:ref:`~PyQt6.QtGui.QImage.pixelIndex`, Pixel Manipulation.
