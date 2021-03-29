.. sip:method-description::
    :status: todo
    :pysig: ad3545c1d916a475f9e390371a6adecb
    :realsig: (int,const QMatrix4x3&)
    :digest: 380dc62504ce4ce9d2ebd31fc519432d

Sets the uniform variable at *location* in the current context to a 4x3 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat4x3, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec3.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
