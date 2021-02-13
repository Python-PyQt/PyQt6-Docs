.. sip:method-description::
    :status: todo
    :pysig: e89a48a6854de773d657200d255ac25c
    :realsig: (const char*,const QMatrix2x4&)
    :digest: 7daa27923387fbe57da8e988fd1e9cd3

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 2x4 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat2x4, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec4.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
