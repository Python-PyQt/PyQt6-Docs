.. sip:method-description::
    :status: todo
    :pysig: cdcc18e14de4aaf0c2a3651c7573779e
    :realsig: (int,const QMatrix3x4&)
    :digest: 380dc62504ce4ce9d2ebd31fc519432d

Sets the uniform variable at *location* in the current context to a 3x4 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat3x4, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec4.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
