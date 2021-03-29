.. sip:method-description::
    :status: todo
    :pysig: f80fb5328658f5f817c26a0c9e5e3392
    :realsig: (QRgb,Qt::MaskMode) const
    :digest: 49bb7be9f253208f5fb2842d9c67d173

Creates and returns a mask for this image based on the given *color* value. If the *mode* is MaskInColor (the default value), all pixels matching *color* will be opaque pixels in the mask. If *mode* is MaskOutColor, all pixels matching the given color will be transparent.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.createAlphaMask`, :sip:ref:`~PyQt6.QtGui.QImage.createHeuristicMask`.
