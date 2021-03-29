.. sip:method-description::
    :status: todo
    :pysig: e1f04ab0c783f2381e14670741eec61d
    :realsig: (bool) const
    :digest: 2696e56ea097093dfc47dbc6b6573de7

Creates and returns a 1-bpp heuristic mask for this image.

The function works by selecting a color from one of the corners, then chipping away pixels of that color starting at all the edges. The four corners vote for which color is to be masked away. In case of a draw (this generally means that this function is not applicable to the image), the result is arbitrary.

The returned image has little-endian bit order (i.e. the image's format is :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_MonoLSB`), which you can convert to big-endian (\ :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono`) using the :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat` function.

If *clipTight* is true (the default) the mask is just large enough to cover the pixels; otherwise, the mask is larger than the data pixels.

Note that this function disregards the alpha buffer.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.createAlphaMask`, Image Transformations.
