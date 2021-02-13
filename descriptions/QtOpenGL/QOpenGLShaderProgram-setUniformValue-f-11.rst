.. sip:method-description::
    :status: todo
    :pysig: 2115574d38a09abf7f145472b607af93
    :realsig: (int,const QMatrix2x3&)
    :digest: 380dc62504ce4ce9d2ebd31fc519432d

Sets the uniform variable at *location* in the current context to a 2x3 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat2x3, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec3.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
