.. sip:method-description::
    :status: todo
    :pysig: 2e0b8f22613494b44c9678f7b212141a
    :realsig: () const
    :digest: c004f153b45dbfb4a3640ad9f69721e3

Returns a QList containing the GPU timestamps taken with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.recordSample`.

This function will block until OpenGL indicates the results are available. It is recommended to check the availability of the result prior to calling this function with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.isResultAvailable`.

**Note:** This function only works on systems that have OpenGL >=3.3 or the ARB_timer_query extension. See :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery` for more details.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.waitForIntervals`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.isResultAvailable`.
