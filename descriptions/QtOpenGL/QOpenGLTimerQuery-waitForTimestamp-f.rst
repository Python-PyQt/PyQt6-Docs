.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e990e5b5fc762520d08408f629e1ef6f

Returns the current timestamp of the GPU when all previously issued OpenGL commands have been received but not necessarily executed by the GPU.

This function blocks until the result is returned.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.recordTimestamp`.
