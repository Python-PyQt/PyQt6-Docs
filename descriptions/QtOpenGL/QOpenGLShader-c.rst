.. sip:class-description::
    :status: todo
    :brief: Allows OpenGL shaders to be compiled
    :digest: d86ef79d4b1465dae724d58d92891fe9

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` class allows OpenGL shaders to be compiled.

This class supports shaders written in the OpenGL Shading Language (GLSL) and in the OpenGL/ES Shading Language (GLSL/ES).

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` shelter the programmer from the details of compiling and linking vertex and fragment shaders.

All data consumed by :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` is expected to be trusted content. Shader source code is passed, possibly after minimal modifications, on to the underlying OpenGL implementation's compiler, which is a black box from Qt's perspective.

**Warning:** Application developers are advised to carefully consider the potential implications before passing in user-provided content to functions such as :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.compileSourceFile`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram`.
