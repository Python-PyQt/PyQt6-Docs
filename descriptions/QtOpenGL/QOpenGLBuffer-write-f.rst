.. sip:method-description::
    :status: todo
    :pysig: 4127c9bbc5bb6e3ccb2bb928688a5c4d
    :realsig: (int,const void*,int)
    :digest: 21ad1423eff02db383ee8772f7c5ee78

Replaces the *count* bytes of this buffer starting at *offset* with the contents of *data*. Any other bytes in the buffer will be left unmodified.

It is assumed that :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create` has been called on this buffer and that it has been bound to the current context.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.read`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.allocate`.
