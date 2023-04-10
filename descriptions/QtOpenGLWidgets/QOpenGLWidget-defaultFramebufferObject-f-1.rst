.. sip:method-description::
    :status: todo
    :pysig: a649616fa7942d7bb9392a6c479d141e
    :realsig: (QOpenGLWidget::TargetBuffer) const
    :digest: bce7b2f45a2af489edbd55037cdde22c

Returns The framebuffer object handle of the specified target buffer or ``0`` if not yet initialized.

Calling this overload only makes sense if :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOption.StereoBuffers` is enabled and supported by the hardware. If not, this method will return the default buffer.

**Note:** The framebuffer object belongs to the context returned by :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context` and may not be accessible from other contexts. The context and the framebuffer object used by the widget changes when reparenting the widget via setParent(). In addition, the framebuffer object changes on each resize.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context`.
