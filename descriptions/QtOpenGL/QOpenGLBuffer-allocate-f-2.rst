.. sip:method-description::
    :status: todo
    :pysig: cb115d0de5e356eef6e4cc9fa6d64a0a
    :realsig: (const void*,int)
    :digest: e7546dda9cc3e78c92e37d0cc686e3fa

Allocates *count* bytes of space to the buffer, initialized to the contents of *data*. Any previous contents will be removed.

It is assumed that :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create` has been called on this buffer and that it has been bound to the current context.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.read`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.write`.
