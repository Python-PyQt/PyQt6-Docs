.. sip:class-description::
    :status: todo
    :brief: Convenience subclass of QWindow to perform OpenGL painting
    :digest: 245859d5b7c2a9b4d5d2b1d86576ca2b

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` class is a convenience subclass of :sip:ref:`~PyQt6.QtGui.QWindow` to perform OpenGL painting.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` is an enhanced :sip:ref:`~PyQt6.QtGui.QWindow` that allows easily creating windows that perform OpenGL rendering using an API that is compatible with :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` Unlike :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` has no dependency on the widgets module and offers better performance.

A typical application will subclass :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` and reimplement the following virtual functions:

* :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.initializeGL` to perform OpenGL resource initialization

* :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.resizeGL` to set up the transformation matrices and other window size dependent resources

* :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` to issue OpenGL commands or draw using :sip:ref:`~PyQt6.QtGui.QPainter`

To schedule a repaint, call the update() function. Note that this will not immediately result in a call to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`. Calling update() multiple times in a row will not change the behavior in any way.

This is a slot so it can be connected to a :sip:ref:`~PyQt6.QtCore.QTimer.timeout` signal to perform animation. Note however that in the modern OpenGL world it is a much better choice to rely on synchronization to the vertical refresh rate of the display. See :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setSwapInterval` on a description of the swap interval. With a swap interval of ``1``, which is the case on most systems by default, the :sip:ref:`~PyQt6.QtGui.QOpenGLContext.swapBuffers` call, that is executed internally by :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` after each repaint, will block and wait for vsync. This means that whenever the swap is done, an update can be scheduled again by calling update(), without relying on timers.

To request a specific configuration for the context, use setFormat() like for any other :sip:ref:`~PyQt6.QtGui.QWindow`. This allows, among others, requesting a given OpenGL version and profile, or enabling depth and stencil buffers.

Unlike :sip:ref:`~PyQt6.QtGui.QWindow`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` allows opening a painter on itself and perform :sip:ref:`~PyQt6.QtGui.QPainter`-based drawing.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` supports multiple update behaviors. The default, ``NoPartialUpdate`` is equivalent to a regular, OpenGL-based :sip:ref:`~PyQt6.QtGui.QWindow`. In contrast, ``PartialUpdateBlit`` and ``PartialUpdateBlend`` are more in line with :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s way of working, where there is always an extra, dedicated framebuffer object present. These modes allow, by sacrificing some performance, redrawing only a smaller area on each paint and having the rest of the content preserved from of the previous frame. This is useful for applications than render incrementally using :sip:ref:`~PyQt6.QtGui.QPainter`, because this way they do not have to redraw the entire window content on each :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` call.

Similarly to :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` supports the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` attribute. When enabled, the OpenGL contexts of all :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` instances will share with each other. This allows accessing each other's shareable OpenGL resources.

For more information on graphics in Qt, see `Graphics <https://doc.qt.io/qt-6/graphicsview.html>`_.
