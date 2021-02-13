.. sip:method-description::
    :status: todo
    :pysig: a6ec9a25fd6831ac18eefa252a14ee62
    :realsig: (QOpenGLTexture::SwizzleComponent,QOpenGLTexture::SwizzleValue)
    :digest: e65496fccc68dd1be1b20f5bf8883444

GLSL shaders are able to reorder the components of the vec4 returned by texture functions. It is also desirable to be able to control this reordering from CPU side code. This is made possible by swizzle masks since OpenGL 3.3.

Each component of the texture can be mapped to one of the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.SwizzleValue.SwizzleValue` options.

This function maps *component* to the output *value*.

**Note:** This function has no effect on Mac and Qt built for OpenGL ES 2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.swizzleMask`.
