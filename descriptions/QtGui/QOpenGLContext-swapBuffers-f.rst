.. sip:method-description::
    :status: todo
    :pysig: 81023c28ced30beca28d538539f09d7c
    :realsig: (QSurface*)
    :digest: 149ddfd211c5b0d6354c908599a1ce97

Swap the back and front buffers of *surface*.

Call this to finish a frame of OpenGL rendering, and make sure to call :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent` again before issuing any further OpenGL commands, for example as part of a new frame.
