.. sip:method-description::
    :status: todo
    :pysig: 53dd04b9581f9f293b7a2469f769a782
    :realsig: (QOpenGLWidget::TargetBuffer)
    :digest: 03e9a609f97da499a62fa96c2f1665b5

Renders and returns a 32-bit RGB image of the framebuffer of the specified target buffer. This overload only makes sense to call when :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOption.StereoBuffers` is enabled. Grabbing the framebuffer of the right target buffer will return the default image if stereoscopic rendering is disabled or if not supported by the hardware.

**Note:** This is a potentially expensive operation because it relies on glReadPixels() to read back the pixels. This may be slow and can stall the GPU pipeline.
