.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e17165c5b4490915f796b2c6aabcf988

Creates a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat` object for specifying the format of an OpenGL framebuffer object.

By default the format specifies a non-multisample framebuffer object with no depth/stencil attachments, texture target ``GL_TEXTURE_2D``, and internal format ``GL_RGBA8``. On OpenGL/ES systems, the default internal format is ``GL_RGBA``.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat.samples`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat.attachment`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat.internalTextureFormat`.
