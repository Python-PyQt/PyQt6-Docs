.. sip:method-description::
    :status: todo
    :pysig: 82efde5731aa68420b578eb847d913c2
    :realsig: (int,int,QOpenGLBuffer::RangeAccessFlags)
    :digest: 8d0ac26ee6ea783fbe59643fb89a8f91

Maps the range specified by *offset* and *count* of the contents of this buffer into the application's memory space and returns a pointer to it. Returns null if memory mapping is not possible. The *access* parameter specifies a combination of access flags.

It is assumed that :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create` has been called on this buffer and that it has been bound to the current context.

**Note:** This function is not available on OpenGL ES 2.0 and earlier.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.unmap`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.bind`.
