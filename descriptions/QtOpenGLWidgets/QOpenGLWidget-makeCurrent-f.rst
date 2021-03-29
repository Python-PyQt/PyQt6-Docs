.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d59e8beffb62e80900bf85e47a76ac17

Prepares for rendering OpenGL content for this widget by making the corresponding context current and binding the framebuffer object in that context.

It is not necessary to call this function in most cases, because it is called automatically before invoking :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.doneCurrent`.
