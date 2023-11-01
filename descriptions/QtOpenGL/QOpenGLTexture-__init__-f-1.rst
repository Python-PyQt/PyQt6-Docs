.. sip:method-description::
    :status: todo
    :pysig: 9b55ab85546b8febf3ffe1e987d7f457
    :realsig: (const QImage&,QOpenGLTexture::MipMapGeneration)
    :digest: 9e571423d8dc373a1961a6db34a727ee

Creates a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` object that can later be bound to the 2D texture target and contains the pixel data contained in *image*. If you wish to have a chain of mipmaps generated then set *genMipMaps* to ``true`` (this is the default).

This does create the underlying OpenGL texture object. Therefore, construction using this constructor does require a valid current OpenGL context.

**Note:** *image* is automatically converted to :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGBA8888` which may have performance implications for large images with a different format.
