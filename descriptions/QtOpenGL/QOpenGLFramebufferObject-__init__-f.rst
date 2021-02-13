.. sip:method-description::
    :status: todo
    :pysig: 56104e8ffaee142c0ccaf19136b13da3
    :realsig: (const QSize&,GLenum)
    :digest: 6c7d3119d8c7251807519979c1c924cc

Constructs an OpenGL framebuffer object and binds a 2D OpenGL texture to the buffer of the size *size*. The texture is bound to the ``GL_COLOR_ATTACHMENT0`` target in the framebuffer object.

The *target* parameter is used to specify the OpenGL texture target. The default target is ``GL_TEXTURE_2D``. Keep in mind that ``GL_TEXTURE_2D`` textures must have a power of 2 width and height (e.g. 256x512), unless you are using OpenGL 2.0 or higher.

By default, no depth and stencil buffers are attached. This behavior can be toggled using one of the overloaded constructors.

The default internal texture format is ``GL_RGBA8`` for desktop OpenGL, and ``GL_RGBA`` for OpenGL/ES.

It is important that you have a current OpenGL context set when creating the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`, otherwise the initialization will fail.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.size`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.texture`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.attachment`.
