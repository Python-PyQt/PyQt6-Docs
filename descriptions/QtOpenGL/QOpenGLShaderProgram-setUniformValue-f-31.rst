.. sip:method-description::
    :status: todo
    :pysig: d57bc70738d7d2cff63c398e9026a65e
    :realsig: (const char*,const QMatrix2x3&)
    :digest: 9d960e2a4e1cb2fc43c65b4c8854cbdc

Sets the uniform variable called *name* in the current context to a 2x3 matrix *value*.

**Note:** This function is not aware of non square matrix support, that is, GLSL types like mat2x3, that is present in modern OpenGL versions. Instead, it treats the uniform as an array of vec3.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue`.
