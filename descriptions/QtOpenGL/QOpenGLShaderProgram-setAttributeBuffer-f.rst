.. sip:method-description::
    :status: todo
    :pysig: 15787a1ff481d5903fd8d63ad92cc53b
    :realsig: (int,GLenum,int,int,int)
    :digest: f4c9117bd7f94a743e3885c6f9ae873c

Sets an array of vertex values on the attribute at *location* in this shader program, starting at a specific *offset* in the currently bound vertex buffer. The *stride* indicates the number of bytes between vertices. A default *stride* value of zero indicates that the vertices are densely packed in the value array.

The *type* indicates the type of elements in the vertex value array, usually ``GL_FLOAT``, ``GL_UNSIGNED_BYTE``, etc. The *tupleSize* indicates the number of components per vertex: 1, 2, 3, or 4.

The array will become active when :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.enableAttributeArray` is called on the *location*. Otherwise the value specified with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue` for *location* will be used.

**Note:** Normalization will be enabled. If this is not desired, call glVertexAttribPointer directly through QOpenGLFunctions.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeArray`.
