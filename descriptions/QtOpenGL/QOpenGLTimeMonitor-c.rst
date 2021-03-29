.. sip:class-description::
    :status: todo
    :brief: Wraps a sequence of OpenGL timer query objects
    :digest: fc1d5878307b7eda26dc0def8af21154

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor` class wraps a sequence of OpenGL timer query objects.

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor` class is a convenience wrapper around a collection of OpenGL timer query objects used to measure intervals of time on the GPU to the level of granularity required by your rendering application.

The OpenGL timer queries objects are queried in sequence to record the GPU timestamps at positions of interest in your rendering code. Once the results for all issues timer queries become available, the results can be fetched and QOpenGLTimerMonitor will calculate the recorded time intervals for you.

The typical use case of this class is to either profile your application's rendering algorithms or to adjust those algorithms in real-time for dynamic performance/quality balancing.

Prior to using :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor` in your rendering function you should set the required number of sample points that you wish to record by calling setSamples(). Note that measuring N sample points will produce N-1 time intervals. Once you have set the number of sample points, call the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.create` function with a valid current OpenGL context to create the necessary query timer objects. These steps are usually performed just once in an initialization function.

Use the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.recordSample` function to delimit blocks of code containing OpenGL commands that you wish to time. You can check availability of the resulting time samples and time intervals with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.isResultAvailable`. The calculated time intervals and the raw timestamp samples can be retrieved with the blocking :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.waitForIntervals` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.waitForSamples` functions respectively.

After retrieving the results and before starting a new round of taking samples (for example, in the next frame) be sure to call the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor.reset` function which will clear the cached results and reset the timer index back to the first timer object.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery`.
