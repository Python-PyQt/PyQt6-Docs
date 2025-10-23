.. sip:method-description::
    :status: todo
    :pysig: f9ad41cf15927aed6c7757f9dc368b77
    :realsig: (const char*,const QMatrix3x2&)
    :digest: 9d960e2a4e1cb2fc43c65b4c8854cbdc

Sets the uniform variable called *name* in the current context to a 3x2 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat3x2, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
