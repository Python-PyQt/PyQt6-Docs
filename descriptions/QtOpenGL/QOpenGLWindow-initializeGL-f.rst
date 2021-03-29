.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 392ac71398581b0cf91c184ba9116582

This virtual function is called once before the first call to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.resizeGL`. Reimplement it in a subclass.

This function should set up any required OpenGL resources and state.

There is no need to call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.makeCurrent` because this has already been done when this function is called. Note however that the framebuffer, in case partial update mode is used, is not yet available at this stage, so avoid issuing draw calls from here. Defer such calls to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` instead.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.resizeGL`.
