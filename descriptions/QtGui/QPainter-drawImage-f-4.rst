.. sip:method-description::
    :status: todo
    :pysig: 3a88669369c88324b49012cdacb131f8
    :realsig: (const QRectF&,const QImage&,const QRectF&,Qt::ImageConversionFlags)
    :digest: 9f27e1322e16ee1451007f10da2951cb

Draws the rectangular portion *source* of the given *image* into the *target* rectangle in the paint device.

**Note:** The image is scaled to fit the rectangle, if both the image and rectangle size disagree.

**Note:** See :ref:`qpainter-drawing-high-resolution-versions-of-pixmaps-and-images` on how this is affected by :sip:ref:`~PyQt6.QtGui.QImage.devicePixelRatio`.

If the image needs to be modified to fit in a lower-resolution result (e.g. converting from 32-bit to 8-bit), use the *flags* to specify how you would prefer this to happen.

+-----------------------------------------------------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|     :lines: 360-365                                                                                 |
+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap`, :sip:ref:`~PyQt6.QtGui.QImage.devicePixelRatio`.
