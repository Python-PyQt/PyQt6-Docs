.. sip:method-description::
    :status: todo
    :pysig: 5c22c8178a94416772c1c1019283d685
    :realsig: (QOpenGLShader::ShaderType, const QByteArray&)
    :digest: ad4b3b9149e20d8a9f447937c8b73953

Compiles *source* as a shader of the specified *type* and adds it to this shader program. Returns ``true`` if compilation was successful, false otherwise. The compilation errors and warnings will be made available via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.

This function is intended to be a short-cut for quickly adding vertex and fragment shaders to a shader program without creating an instance of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` first.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.removeShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.removeAllShaders`.
