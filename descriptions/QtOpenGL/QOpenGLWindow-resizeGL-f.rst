.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 6b4080e611e6abec2fb251dd439ccea0

This virtual function is called whenever the widget has been resized. Reimplement it in a subclass. The new size is passed in *w* and *h*.

**Note:** This is merely a convenience function in order to provide an API that is compatible with :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`. Unlike with :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, derived classes are free to choose to override :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.resizeEvent` instead of this function.

**Note:** Avoid issuing OpenGL commands from this function as there may not be a context current when it is invoked. If it cannot be avoided, call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.makeCurrent`.

**Note:** Scheduling updates from here is not necessary. The windowing systems will send expose events that trigger an update automatically.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.initializeGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`.
