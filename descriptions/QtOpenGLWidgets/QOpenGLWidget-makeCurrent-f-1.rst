.. sip:method-description::
    :status: todo
    :pysig: 45774b267c3fa6d39c5262b3383c859c
    :realsig: (QOpenGLWidget::TargetBuffer)
    :digest: 563a3eced75bb6ea87ba35023c1e81e9

Prepares for rendering OpenGL content for this widget by making the context for the passed in buffer current and binding the framebuffer object in that context.

**Note:** This only makes sense to call when stereoscopic rendering is enabled. Nothing will happen if the right buffer is requested when it's disabled.

It is not necessary to call this function in most cases, because it is called automatically before invoking :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.doneCurrent`.
