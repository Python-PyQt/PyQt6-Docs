.. sip:method-description::
    :status: todo
    :pysig: 5a2ff704e4aa2facb87261cdf62ad554
    :realsig: (int,void*,int)
    :digest: d172d5a704c689fab5d5b3d93e1a7f51

Reads the *count* bytes in this buffer starting at *offset* into *data*. Returns ``true`` on success; false if reading from the buffer is not supported. Buffer reading is not supported under OpenGL/ES.

It is assumed that this buffer has been bound to the current context.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.write`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.bind`.
