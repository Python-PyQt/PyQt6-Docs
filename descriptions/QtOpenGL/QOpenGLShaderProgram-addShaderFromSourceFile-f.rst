.. sip:method-description::
    :status: todo
    :pysig: 7479ae58b3c0efe0492ae7e9551ab592
    :realsig: (QOpenGLShader::ShaderType,const QString&)
    :digest: aa299ec49c85b4ab473f0bfeebc6a2e6

Compiles the contents of *fileName* as a shader of the specified *type* and adds it to this shader program. Returns ``true`` if compilation was successful, false otherwise. The compilation errors and warnings will be made available via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.

This function is intended to be a short-cut for quickly adding vertex and fragment shaders to a shader program without creating an instance of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` first.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`.
