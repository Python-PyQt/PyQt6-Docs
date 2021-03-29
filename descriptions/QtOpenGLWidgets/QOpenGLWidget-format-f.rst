.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: () const
    :digest: 67fa817ec61ea0f28379b13f062f8a29

Returns the context and surface format used by this widget and its toplevel window.

After the widget and its toplevel have both been created, resized and shown, this function will return the actual format of the context. This may differ from the requested format if the request could not be fulfilled by the platform. It is also possible to get larger color buffer sizes than requested.

When the widget's window and the related OpenGL resources are not yet initialized, the return value is the format that has been set via :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context`.
