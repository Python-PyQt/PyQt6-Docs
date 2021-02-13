.. sip:enum-description::
    :status: todo
    :digest: e936c17f4a490faa3a0a559fd72e1889

Defines the modes supported for digital image compositing. Composition modes are used to specify how the pixels in one image, the source, are merged with the pixel in another image, the destination.

Please note that the bitwise raster operation modes, denoted with a RasterOp prefix, are only natively supported in the X11 and raster paint engines. This means that the only way to utilize these modes on the Mac is via a :sip:ref:`~PyQt6.QtGui.QImage`. The RasterOp denoted blend modes are *not* supported for pens and brushes with alpha components. Also, turning on the :sip:ref:`~PyQt6.QtGui.QPainter.RenderHints.Antialiasing` render hint will effectively disable the RasterOp modes.

.. image:: ../../../images/qpainter-compositionmode1.png

.. image:: ../../../images/qpainter-compositionmode2.png

The most common type is SourceOver (often referred to as just alpha blending) where the source pixel is blended on top of the destination pixel in such a way that the alpha component of the source defines the translucency of the pixel.

Several composition modes require an alpha channel in the source or target images to have an effect. For optimal performance the image format :sip:ref:`~PyQt6.QtGui.QImage.Format` is preferred.

When a composition mode is set it applies to all painting operator, pens, brushes, gradients and pixmap/image drawing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.compositionMode`, :sip:ref:`~PyQt6.QtGui.QPainter.setCompositionMode`, Composition Modes, `Image Composition Example <https://doc.qt.io/qt-6/qtwidgets-painting-imagecomposition-example.html>`_.
