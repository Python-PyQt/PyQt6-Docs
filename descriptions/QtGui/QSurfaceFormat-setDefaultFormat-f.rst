.. sip:method-description::
    :status: todo
    :pysig: 44457fd5e93fdede3a397e0ec120c714
    :realsig: (const QSurfaceFormat&)
    :digest: 0237e7ca5c64129529a0360be1bb6620

Sets the global default surface *format*.

This format is used by default in :sip:ref:`~PyQt6.QtGui.QOpenGLContext`, :sip:ref:`~PyQt6.QtGui.QWindow`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and similar classes.

It can always be overridden on a per-instance basis by using the class in question's own setFormat() function. However, it is often more convenient to set the format for all windows once at the start of the application. It also guarantees proper behavior in cases where shared contexts are required, because setting the format via this function guarantees that all contexts and surfaces, even the ones created internally by Qt, will use the same format.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.defaultFormat`.
