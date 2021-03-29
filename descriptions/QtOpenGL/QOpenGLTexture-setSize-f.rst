.. sip:method-description::
    :status: todo
    :pysig: 25b8fd7c923034fbf04dc84474d6ae55
    :realsig: (int,int,int)
    :digest: a0c0112a3332394047aa51063eee7be8

Sets the dimensions of this texture object to *width*, *height*, and *depth*. The default for each dimension is 1. The maximum allowable texture size is dependent upon your OpenGL implementation. Allocating storage for a texture less than the maximum size can still fail if your system is low on resources.

If a non-power-of-two *width*, *height* or *depth* is provided and your OpenGL implementation doesn't have support for repeating non-power-of-two textures, then the wrap mode is automatically set to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.WrapMode.ClampToEdge`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.width`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.height`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.depth`.
