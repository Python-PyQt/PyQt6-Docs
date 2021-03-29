.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 92a36b2c3cf09f885de68236a3b1e99e

For 32-bit images, this function is equivalent to :sip:ref:`~PyQt6.QtGui.QImage.allGray`.

For color indexed images, this function returns ``true`` if color(i) is QRgb(i, i, i) for all indexes of the color table; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.allGray`, Image Formats.
