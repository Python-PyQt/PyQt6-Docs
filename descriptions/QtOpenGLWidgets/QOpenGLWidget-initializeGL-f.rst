.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3f534267191beb201ad8e185d79d5d8a

This virtual function is called once before the first call to :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` or :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL`. Reimplement it in a subclass.

This function should set up any required OpenGL resources.

There is no need to call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` because this has already been done when this function is called. Note however that the framebuffer is not yet available at this stage, so avoid issuing draw calls from here. Defer such calls to :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` instead.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL`.
