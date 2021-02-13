.. sip:method-description::
    :status: todo
    :pysig: 2f2b473cc1d478326f97f563c8b26422
    :realsig: (const char*,GLenum,int,int,int)
    :digest: 4bdba8efa4debd8e0533350cc41cd27b

This is an overloaded function.

Sets an array of vertex values on the attribute called *name* in this shader program, starting at a specific *offset* in the currently bound vertex buffer. The *stride* indicates the number of bytes between vertices. A default *stride* value of zero indicates that the vertices are densely packed in the value array.

The *type* indicates the type of elements in the vertex value array, usually ``GL_FLOAT``, ``GL_UNSIGNED_BYTE``, etc. The *tupleSize* indicates the number of components per vertex: 1, 2, 3, or 4.

The array will become active when :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.enableAttributeArray` is called on the *name*. Otherwise the value specified with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue` for *name* will be used.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeArray`.
