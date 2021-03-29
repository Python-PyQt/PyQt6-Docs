.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 46e42a7101f9d9fbcc5b20e148911bd7

Places a marker in the OpenGL command queue for the GPU to record the timestamp when this marker is reached by the GPU. This function is non-blocking and the result will become available at some later time.

The availability of the result can be checked with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.isResultAvailable`. The result can be fetched with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.waitForResult` which will block if the result is not yet available.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.waitForResult`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.isResultAvailable`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.begin`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.end`.
