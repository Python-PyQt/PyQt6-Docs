.. sip:class-description::
    :status: todo
    :brief: Represents an offscreen surface in the underlying platform
    :digest: 5e2e44d93b20a6c85c1b43361c793a4c

The :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` class represents an offscreen surface in the underlying platform.

:sip:ref:`~PyQt6.QtGui.QOffscreenSurface` is intended to be used with `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ to allow rendering with OpenGL in an arbitrary thread without the need to create a :sip:ref:`~PyQt6.QtGui.QWindow`.

Even though the surface is typically renderable, the surface's pixels are not accessible. :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` should only be used to create OpenGL resources such as textures or framebuffer objects.

An application will typically use :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` to perform some time-consuming tasks in a separate thread in order to avoid stalling the main rendering thread. Resources created in the :sip:ref:`~PyQt6.QtGui.QOffscreenSurface`'s context can be shared with the main OpenGL context. Some common use cases are asynchronous texture uploads or rendering into a QOpenGLFramebufferObject.

How the offscreen surface is implemented depends on the underlying platform, but it will typically use a pixel buffer (pbuffer). If the platform doesn't implement or support offscreen surfaces, :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` will use an invisible :sip:ref:`~PyQt6.QtGui.QWindow` internally.

**Note:** Due to the fact that :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` is backed by a :sip:ref:`~PyQt6.QtGui.QWindow` on some platforms, cross-platform applications must ensure that :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.create` is only called on the main (GUI) thread. The :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` is then safe to be used with :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent` on other threads, but the initialization and destruction must always happen on the main (GUI) thread.

**Note:** In order to create an offscreen surface that is guaranteed to be compatible with a given context and window, make sure to set the format to the context's or the window's actual format, that is, the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` returned from :sip:ref:`~PyQt6.QtGui.QOpenGLContext.format` or :sip:ref:`~PyQt6.QtGui.QWindow.format` *after the context or window has been created*. Passing the format returned from :sip:ref:`~PyQt6.QtGui.QWindow.requestedFormat` to :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.setFormat` may result in an incompatible offscreen surface since the underlying windowing system interface may offer a different set of configurations for window and pbuffer surfaces.

**Note:** Some platforms may utilize a surfaceless context extension (for example EGL_KHR_surfaceless_context) when available. In this case there will be no underlying native surface. For the use cases of :sip:ref:`~PyQt6.QtGui.QOffscreenSurface` (rendering to FBOs, texture upload) this is not a problem.
