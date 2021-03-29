.. sip:method-description::
    :status: todo
    :pysig: ad3be725aaea53e6102a2d971fe70b17
    :realsig: (int,const QMatrix4x2&)
    :digest: 380dc62504ce4ce9d2ebd31fc519432d

Sets the uniform variable at *location* in the current context to a 4x2 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat4x2, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
