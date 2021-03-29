.. sip:method-description::
    :status: todo
    :pysig: 42433b7af77ab2f97d1dec37d1669f6b
    :realsig: (const QSize&,QOpenGLFramebufferObject::Attachment,GLenum,GLenum)
    :digest: d7b0621a145eaa6863b3be8bfdbaf711

Constructs an OpenGL framebuffer object and binds a texture to the buffer of the given *size*.

The *attachment* parameter describes the depth/stencil buffer configuration, *target* the texture target and *internalFormat* the internal texture format. The default texture target is ``GL_TEXTURE_2D``, while the default internal format is ``GL_RGBA8`` for desktop OpenGL and ``GL_RGBA`` for OpenGL/ES.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.size`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.texture`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.attachment`.
