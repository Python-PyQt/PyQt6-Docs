.. sip:method-description::
    :status: todo
    :pysig: 3bb580219793d6e3022d378980acdc50
    :realsig: (int,int,QOpenGLFramebufferObject::Attachment,GLenum,GLenum)
    :digest: 65722165000bc951dc36b38f5c1f9f48

Constructs an OpenGL framebuffer object and binds a texture to the buffer of the given *width* and *height*.

The *attachment* parameter describes the depth/stencil buffer configuration, *target* the texture target and *internalFormat* the internal texture format. The default texture target is ``GL_TEXTURE_2D``, while the default internal format is ``GL_RGBA8`` for desktop OpenGL and ``GL_RGBA`` for OpenGL/ES.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.size`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.texture`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.attachment`.
