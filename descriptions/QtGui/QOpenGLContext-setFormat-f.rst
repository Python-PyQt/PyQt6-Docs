.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: (const QSurfaceFormat&)
    :digest: 8a90cf72220e0e92065158fb41797179

Sets the *format* the OpenGL context should be compatible with. You need to call :sip:ref:`~PyQt6.QtGui.QOpenGLContext.create` before it takes effect.

When the format is not explicitly set via this function, the format returned by :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.defaultFormat` will be used. This means that when having multiple contexts, individual calls to this function can be replaced by one single call to :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` before creating the first context.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOpenGLContext.format`.
