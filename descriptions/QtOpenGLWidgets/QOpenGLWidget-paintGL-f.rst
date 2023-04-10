.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5018e1d2eb6ee243bcb35fc4355fcd7e

This virtual function is called whenever the widget needs to be painted. Reimplement it in a subclass.

There is no need to call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` because this has already been done when this function is called.

Before invoking this function, the context and the framebuffer are bound, and the viewport is set up by a call to glViewport(). No other state is set and no clearing or drawing is performed by the framework.

When :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOption.StereoBuffers` is enabled, this function will be called twice - once for each buffer. Query what buffer is currently bound by calling :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.currentTargetBuffer`.

**Note:** The framebuffer of each target will be drawn to even when stereoscopic rendering is not supported by the hardware. Only the left buffer will actually be visible in the window.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.currentTargetBuffer`.
