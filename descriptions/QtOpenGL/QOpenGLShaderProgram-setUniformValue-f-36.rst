.. sip:method-description::
    :status: todo
    :pysig: 7645eae5ae3417a4fdf271d01201a884
    :realsig: (const char*,const QMatrix4x2&)
    :digest: 9d960e2a4e1cb2fc43c65b4c8854cbdc

Sets the uniform variable called *name* in the current context to a 4x2 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat4x2, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
