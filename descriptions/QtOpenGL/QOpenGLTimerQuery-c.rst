.. sip:class-description::
    :status: todo
    :brief: Wraps an OpenGL timer query object
    :digest: d95ede54937fa4af7d88585cd0b3a3a3

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery` class wraps an OpenGL timer query object.

OpenGL timer query objects are OpenGL managed resources to measure the execution times of sequences of OpenGL commands on the GPU.

OpenGL offers various levels of support for timer queries, depending on the version of OpenGL you have and the presence of the ARB_timer_query or EXT_timer_query extensions. The support can be summarized as:

* OpenGL >=3.3 offers full support for all timer query functionality.

* OpenGL 3.2 with the ARB_timer_query extension offers full support for all timer query functionality.

* OpenGL <=3.2 with the EXT_timer_query extension offers limited support in that the timestamp of the GPU cannot be queried. Places where this impacts functions provided by Qt classes will be highlighted in the function documentation.

* OpenGL ES 2 (and OpenGL ES 3) do not provide any support for OpenGL timer queries.

OpenGL represents time with a granularity of 1 nanosecond (1e-9 seconds). As a consequence of this, 32-bit integers would only give a total possible duration of approximately 4 seconds, which would not be difficult to exceed in poorly performing or lengthy operations. OpenGL therefore uses 64 bit integer types to represent times. A GLuint64 variable has enough width to contain a duration of hundreds of years, which is plenty for real-time rendering needs.

As with the other Qt OpenGL classes, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery` has a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.create` function to create the underlying OpenGL object. This is to allow the developer to ensure that there is a valid current OpenGL context at the time.

Once created, timer queries can be issued in one of several ways. The simplest method is to delimit a block of commands with calls to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.begin` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.end`. This instructs OpenGL to measure the time taken from completing all commands issued prior to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.begin` until the completion of all commands issued prior to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.end`.

At the end of a frame we can retrieve the results by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.waitForResult`. As this function's name implies, it blocks CPU execution until OpenGL notifies that the timer query result is available. To avoid blocking, you can check if the query result is available by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.isResultAvailable`. Note that modern GPUs are deeply pipelined and query results may not become available for between 1-5 frames after they were issued.

Note that OpenGL does not permit nesting or interleaving of multiple timer queries using :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.begin` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.end`. Using multiple timer queries and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.recordTimestamp` avoids this limitation. When using :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.recordTimestamp` the result can be obtained at some later time using :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.isResultAvailable` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.waitForResult`. Qt provides the convenience class :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor` that helps with using multiple query objects.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimeMonitor`.
