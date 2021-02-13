.. sip:method-description::
    :status: todo
    :pysig: 44457fd5e93fdede3a397e0ec120c714
    :realsig: (const QSurfaceFormat&)
    :digest: 3dd2cfb78c6a70e65fe8c01eab26eb79

Sets the global default surface *format*.

This format is used by default in `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_, :sip:ref:`~PyQt6.QtGui.QWindow`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and similar classes.

It can always be overridden on a per-instance basis by using the class in question's own setFormat() function. However, it is often more convenient to set the format for all windows once at the start of the application. It also guarantees proper behavior in cases where shared contexts are required, because settings the format via this function guarantees that all contexts and surfaces, even the ones created internally by Qt, will use the same format.

**Note:** When setting :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts`, it is strongly recommended to place the call to this function before the construction of the :sip:ref:`~PyQt6.QtGui.QGuiApplication` or :sip:ref:`~PyQt6.QtWidgets.QApplication`. Otherwise *format* will not be applied to the global share context and therefore issues may arise with context sharing afterwards.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.defaultFormat`.
