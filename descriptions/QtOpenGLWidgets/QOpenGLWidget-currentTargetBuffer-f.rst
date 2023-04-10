.. sip:method-description::
    :status: todo
    :pysig: 45774b267c3fa6d39c5262b3383c859c
    :realsig: () const
    :digest: b8971064e2270a4c3fb947d4f94f41e3

Returns the currently active target buffer. This will be the left buffer by default, the right buffer is only used when :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOption.StereoBuffers` is enabled. When stereoscopic rendering is enabled, this can be queried in :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` to know what buffer is currently in use. :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` will be called twice, once for each target.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`.
