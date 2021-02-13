.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (GLenum)
    :digest: 86bc8614465b17f5a5bbb296b78da23a

Sets a custom internal texture format of *texFormat*.

When working with sRGB framebuffers, it will be necessary to specify a format like ``GL_SRGB8_ALPHA8``. This can be achieved by calling this function.

**Note:** This function has no effect if called after the widget has already been shown and thus it performed initialization.

**Note:** This function will typically have to be used in combination with a :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` call that sets the color space to QSurfaceFormat::sRGBColorSpace.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.textureFormat`.
