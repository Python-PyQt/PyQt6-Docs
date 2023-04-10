.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,QRgb)
    :digest: bd3f00dabc7c635f938a28d28694ff1d

Sets the color at the given *index* in the color table, to the given to *colorValue*. The color value is an ARGB quadruplet.

If *index* is outside the current size of the color table, it is expanded with setColorCount().

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.colorCount`, Pixel Manipulation, :sip:ref:`~PyQt6.QtGui.QImage.color`.
