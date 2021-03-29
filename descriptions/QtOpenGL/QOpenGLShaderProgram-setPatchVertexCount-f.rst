.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: f5b55764b34a6d0cc6f899250c191d06

Use this function to specify to OpenGL the number of vertices in a patch to *count*. A patch is a custom OpenGL primitive whose interpretation is entirely defined by the tessellation shader stages. Therefore, calling this function only makes sense when using a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` containing tessellation stage shaders. When using OpenGL tessellation, the only primitive that can be rendered with ``glDraw\*()`` functions is ``GL_PATCHES``.

This is equivalent to calling glPatchParameteri(GL_PATCH_VERTICES, count).

**Note:** This modifies global OpenGL state and is not specific to this :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` instance. You should call this in your render function when needed, as :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` will not apply this for you. This is purely a convenience function.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.patchVertexCount`.
