.. sip:method-description::
    :status: todo
    :pysig: 2e441b58670b7464efda498086f11a94
    :realsig: () const
    :digest: 1275813c426b0ffa3bc0587dc4fe9243

Accessor function for whether the alpha channel is used or not.

Sometimes the pixel format reserves place for an alpha channel, so :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaSize` will return > 0, but the alpha channel is not used/ignored.

For example, for :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32`, the :sip:ref:`~PyQt6.QtGui.QPixelFormat.bitsPerPixel` is 32, because the alpha channel has a size of 8, but alphaUsage() reflects :sip:ref:`~PyQt6.QtGui.QPixelFormat.AlphaUsage.IgnoresAlpha`.

Note that in such situations the :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaPosition` of the unused alpha channel is still important, as it affects the placement of the color channels.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaPosition`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaSize`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.premultiplied`.
