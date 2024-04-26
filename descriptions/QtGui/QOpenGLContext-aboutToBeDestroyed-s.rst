.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 047889456ba81ad234fda750e5c9ec91

This signal is emitted before the underlying native OpenGL context is destroyed, such that users may clean up OpenGL resources that might otherwise be left dangling in the case of shared OpenGL contexts.

If you wish to make the context current in order to do clean-up, make sure to only connect to the signal using a direct connection.

**Note:** In Qt for Python, this signal will not be received when emitted from the destructor of :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` due to the Python instance already being destroyed. We recommend doing cleanups in :sip:ref:`~PyQt6.QtWidgets.QWidget.hideEvent` instead.
