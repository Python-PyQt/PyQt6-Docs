.. sip:method-description::
    :status: todo
    :pysig: 496e7f86ea94517316f11ba33b1e7343
    :realsig: (GLenum)
    :digest: 3c9161f68927222ae9a72e85523d7541

Binds the graphics resources used by the blitter. This must be called before calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit`. Code modifying the OpenGL state should be avoided between the call to  and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit` because otherwise conflicts may arise.

*target* is the texture target for the source texture and must be either ``GL_TEXTURE_2D``, ``GL_TEXTURE_RECTANGLE``, or ``GL_OES_EGL_image_external``.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.release`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit`.
