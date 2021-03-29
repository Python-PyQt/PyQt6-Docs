.. sip:method-description::
    :status: todo
    :pysig: a9d516bcbada33afc6b36cbe1cdd9ded
    :realsig: (QSurface::SurfaceType)
    :digest: 1c210572acc433744ba52a1d2382eeec

Sets the *surfaceType* of the window.

Specifies whether the window is meant for raster rendering with :sip:ref:`~PyQt6.QtGui.QBackingStore`, or OpenGL rendering with `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_.

The :sip:ref:`~PyQt6.QtGui.QWindow.surfaceType` will be used when the native surface is created in the :sip:ref:`~PyQt6.QtGui.QWindow.create` function. Calling this function after the native surface has been created requires calling :sip:ref:`~PyQt6.QtGui.QWindow.destroy` and :sip:ref:`~PyQt6.QtGui.QWindow.create` to release the old native surface and create a new one.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.surfaceType`, :sip:ref:`~PyQt6.QtGui.QBackingStore`, `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_, :sip:ref:`~PyQt6.QtGui.QWindow.create`, :sip:ref:`~PyQt6.QtGui.QWindow.destroy`.
