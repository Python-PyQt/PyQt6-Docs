.. sip:method-description::
    :status: todo
    :pysig: 74672e6a503348082c148466f28c9fae
    :realsig: (const QRectF&,const QImage&,const QRectF&,Qt::ImageConversionFlags)
    :digest: 820985a70232553004a0485c382b7f25

Draws the rectangular portion *source* of the given *image* into the *target* rectangle in the paint device.

**Note:** The image is scaled to fit the rectangle, if both the image and rectangle size disagree.

**Note:** See :ref:`qpainter-drawing-high-resolution-versions-of-pixmaps-and-images` on how this is affected by QImage::devicePixelRatio().

If the image needs to be modified to fit in a lower-resolution result (e.g. converting from 32-bit to 8-bit), use the *flags* to specify how you would prefer this to happen.

+-----------------------------------------------------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|     :lines: 360-365                                                                                 |
+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap`.
