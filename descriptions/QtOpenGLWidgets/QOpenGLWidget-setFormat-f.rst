.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: (const QSurfaceFormat&)
    :digest: ee86fd6eda98ced4fc850fc4baf2242a

Sets the requested surface *format*.

When the format is not explicitly set via this function, the format returned by :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.defaultFormat` will be used. This means that when having multiple OpenGL widgets, individual calls to this function can be replaced by one single call to :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` before creating the first widget.

**Note:** Requesting an alpha buffer via this function will not lead to the desired results when the intention is to make other widgets beneath visible. Instead, use :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop` to enable semi-transparent :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` instances with other widgets visible underneath. Keep in mind however that this breaks the stacking order, so it will no longer be possible to have other widgets on top of the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.format`, :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop`, :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat`.
