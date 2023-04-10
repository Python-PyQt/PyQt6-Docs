.. sip:method-description::
    :status: todo
    :pysig: a8c229928ee22986fded27ccadf38348
    :realsig: (bool) const
    :digest: 9083c6f41e3403efafbcf1411748a5fb

Returns the contents of this framebuffer object as a :sip:ref:`~PyQt6.QtGui.QImage`.

If *flipped* is true the image is flipped from OpenGL coordinates to raster coordinates. If used together with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice`, *flipped* should be the opposite of the value of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice.paintFlipped`.

The returned image has a format of premultiplied ARGB32 or RGB32. The latter is used only when internalTextureFormat() is set to ``GL_RGB``. Since Qt 5.2 the function will fall back to premultiplied RGBA8888 or RGBx8888 when reading to (A)RGB32 is not supported, and this includes OpenGL ES. Since Qt 5.4 an A2BGR30 image is returned if the internal format is RGB10_A2, and since Qt 5.12 a RGBA64 image is return if the internal format is RGBA16.

If the rendering in the framebuffer was not done with premultiplied alpha in mind, create a wrapper :sip:ref:`~PyQt6.QtGui.QImage` with a non-premultiplied format. This is necessary before performing operations like QImage::save() because otherwise the image data would get unpremultiplied, even though it was not premultiplied in the first place. To create such a wrapper without performing a copy of the pixel data, do the following:

::

    QImage fboImage(fbo.toImage());
    QImage image(fboImage.constBits(), fboImage.width(), fboImage.height(), QImage::Format_ARGB32);

For multisampled framebuffer objects the samples are resolved using the ``GL_EXT_framebuffer_blit`` extension. If the extension is not available, the contents of the returned image is undefined.

For singlesampled framebuffers the contents is retrieved via ``glReadPixels``. This is a potentially expensive and inefficient operation. Therefore it is recommended that this function is used as seldom as possible.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice.paintFlipped`.
