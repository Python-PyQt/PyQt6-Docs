.. sip:method-description::
    :status: todo
    :pysig: 00066c6edc02d21499e11800ae81eea3
    :realsig: (QOpenGLTexture::DepthStencilMode)
    :digest: 4443eee26cab8c20e6c5cfc96c8b7cdd

If using a texture that has a combined depth/stencil format this function sets which component of the texture is accessed to *mode*.

When the parameter is set to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.DepthStencilMode.DepthMode`, then accessing it from the shader will access the depth component as a single float, as normal. But when the parameter is set to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.DepthStencilMode.StencilMode`, the shader will access the stencil component.

**Note:** This function has no effect on Mac and Qt built for OpenGL ES 2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.depthStencilMode`.
