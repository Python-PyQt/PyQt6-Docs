.. sip:method-description::
    :status: todo
    :pysig: e89a48a6854de773d657200d255ac25c
    :realsig: (const char*,const QMatrix2x4&)
    :digest: 9d960e2a4e1cb2fc43c65b4c8854cbdc

Sets the uniform variable called *name* in the current context to a 2x4 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat2x4, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec4.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
