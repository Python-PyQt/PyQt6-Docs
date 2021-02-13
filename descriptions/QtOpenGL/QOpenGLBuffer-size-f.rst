.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 37ee01b4727313a89a6aab58a0922791

Returns the size of the data in this buffer, for reading operations. Returns -1 if fetching the buffer size is not supported, or the buffer has not been created.

It is assumed that this buffer has been bound to the current context.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.isCreated`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.bind`.
