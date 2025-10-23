.. sip:method-description::
    :status: todo
    :pysig: 0e0756385e2463bc6ff37f1eb4d4133b
    :realsig: (const char*,const QMatrix3x4&)
    :digest: 9d960e2a4e1cb2fc43c65b4c8854cbdc

Sets the uniform variable called *name* in the current context to a 3x4 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat3x4, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec4.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
