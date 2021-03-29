.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: 96378e71ffb715a82117951baa07d769

Issues an OpenGL timer query at this point in the OpenGL command queue. Calling this function in a sequence in your application's rendering function, will build up details of the GPU time taken to execute the OpenGL commands between successive calls to this function.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.setSampleCount`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.isResultAvailable`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.waitForSamples`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.waitForIntervals`.
