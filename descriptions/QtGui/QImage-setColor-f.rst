.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,QRgb)
    :digest: 366c6d4cf03fc87da4eee4c1f85ec262

Sets the color at the given *index* in the color table, to the given to *colorValue*. The color value is an ARGB quadruplet.

If *index* is outside the current size of the color table, it is expanded with :sip:ref:`~PyQt6.QtGui.QImage.setColorCount`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.color`, :sip:ref:`~PyQt6.QtGui.QImage.colorCount`, :sip:ref:`~PyQt6.QtGui.QImage.setColorTable`, Pixel Manipulation.
