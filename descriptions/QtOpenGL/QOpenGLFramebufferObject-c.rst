.. sip:class-description::
    :status: todo
    :brief: Encapsulates an OpenGL framebuffer object
    :digest: 4a452a8e69b3f48748471f1bfcb5942f

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject` class encapsulates an OpenGL framebuffer object.

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject` class encapsulates an OpenGL framebuffer object, defined by the ``GL_EXT_framebuffer_object`` extension. It provides a rendering surface that can be painted on with a :sip:ref:`~PyQt6.QtGui.QPainter` with the help of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice`, or rendered to using native OpenGL calls. This surface can be bound and used as a regular texture in your own OpenGL drawing code. By default, the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject` class generates a 2D OpenGL texture (using the ``GL_TEXTURE_2D`` target), which is used as the internal rendering target.

**It is important to have a current OpenGL context when creating a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`, otherwise initialization will fail.**

Create the QOpenGLFrameBufferObject instance with the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment.CombinedDepthStencil` attachment if you want :sip:ref:`~PyQt6.QtGui.QPainter` to render correctly. Note that you need to create a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject` with more than one sample per pixel for primitives to be antialiased when drawing using a :sip:ref:`~PyQt6.QtGui.QPainter`. To create a multisample framebuffer object you should use one of the constructors that take a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat` parameter, and set the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat.samples` property to a non-zero value.

For multisample framebuffer objects a color render buffer is created, otherwise a texture with the specified texture target is created. The color render buffer or texture will have the specified internal format, and will be bound to the ``GL_COLOR_ATTACHMENT0`` attachment in the framebuffer object.

Multiple render targets are also supported, in case the OpenGL implementation supports this. Here there will be multiple textures (or, in case of multisampling, renderbuffers) present and each of them will get attached to ``GL_COLOR_ATTACHMENT0``, ``1``, ``2``, ...

If you want to use a framebuffer object with multisampling enabled as a texture, you first need to copy from it to a regular framebuffer object using QOpenGLContext::blitFramebuffer().

It is possible to draw into a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject` using :sip:ref:`~PyQt6.QtGui.QPainter` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice` in a separate thread.
