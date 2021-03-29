.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 60d78e89a7dff425b4147d0a6e57086d

This virtual function is called whenever the widget needs to be painted. Reimplement it in a subclass.

There is no need to call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` because this has already been done when this function is called.

Before invoking this function, the context and the framebuffer are bound, and the viewport is set up by a call to glViewport(). No other state is set and no clearing or drawing is performed by the framework.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL`.
