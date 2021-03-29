.. sip:method-description::
    :status: todo
    :pysig: fd4d564ddac9475ab8addb0d0fbbd846
    :realsig: (const QSize&,GLenum)
    :digest: 964bd43e5d76359c2b060b4a1399f00c

Creates and attaches an additional texture or renderbuffer of *size* width and height.

There is always an attachment at GL_COLOR_ATTACHMENT0. Call this function to set up additional attachments at GL_COLOR_ATTACHMENT1, GL_COLOR_ATTACHMENT2, ...

When *internalFormat* is not ``0``, it specifies the internal format of the texture or renderbuffer. Otherwise a default of GL_RGBA or GL_RGBA8 is used.

**Note:** This is only functional when multiple render targets are supported by the OpenGL implementation. When that is not the case, the function will not add any additional color attachments. Call QOpenGLFunctions::hasOpenGLFeature() with QOpenGLFunctions::MultipleRenderTargets at runtime to check if MRT is supported.

**Note:** The internal format of the color attachments may differ but there may be limitations on the supported combinations, depending on the drivers.

**Note:** The size of the color attachments may differ but rendering is limited to the area that fits all the attachments, according to the OpenGL specification. Some drivers may not be fully conformant in this respect, however.
