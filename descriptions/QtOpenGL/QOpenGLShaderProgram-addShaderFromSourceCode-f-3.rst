.. sip:method-description::
    :status: todo
    :pysig: 1838ddf71a6a6d561fdc433dc1aca19a
    :realsig: (QOpenGLShader::ShaderType,const QString&)
    :digest: 7b4c0fef8ab57d43fb6ba5e061a48c17

This is an overloaded function.

Compiles *source* as a shader of the specified *type* and adds it to this shader program. Returns ``true`` if compilation was successful, false otherwise. The compilation errors and warnings will be made available via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.

This function is intended to be a short-cut for quickly adding vertex and fragment shaders to a shader program without creating an instance of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` first.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.removeShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.removeAllShaders`.
