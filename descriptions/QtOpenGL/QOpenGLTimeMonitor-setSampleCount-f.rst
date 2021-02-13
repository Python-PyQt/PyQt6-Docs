.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 778250bb5825b236d4cbfd340c3fa5f0

Sets the number of sample points to *sampleCount*. After setting the number of samples with this function, you must call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.create` to instantiate the underlying OpenGL timer query objects.

The new *sampleCount* must be at least 2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.sampleCount`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.create`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.recordSample`.
