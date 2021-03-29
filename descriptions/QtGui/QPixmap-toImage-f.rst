.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: () const
    :digest: b1ea2f42a0e33d56410369693557c256

Converts the pixmap to a :sip:ref:`~PyQt6.QtGui.QImage`. Returns a null image if the conversion fails.

If the pixmap has 1-bit depth, the returned image will also be 1 bit deep. Images with more bits will be returned in a format closely represents the underlying system. Usually this will be :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32_Premultiplied` for pixmaps with an alpha and :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32` or :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB16` for pixmaps without alpha.

Note that for the moment, alpha masks on monochrome images are ignored.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage`, Image Formats.
