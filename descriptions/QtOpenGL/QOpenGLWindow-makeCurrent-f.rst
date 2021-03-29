.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 577f6395b89036f173c3aa3b75698622

Prepares for rendering OpenGL content for this window by making the corresponding context current and binding the framebuffer object, if there is one, in that context context.

It is not necessary to call this function in most cases, because it is called automatically before invoking :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`. It is provided nonetheless to support advanced, multi-threaded scenarios where a thread different than the GUI or main thread may want to update the surface or framebuffer contents. See `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ for more information on threading related issues.

This function is suitable for calling also when the underlying platform window is already destroyed. This means that it is safe to call this function from a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` subclass' destructor. If there is no native window anymore, an offscreen surface is used instead. This ensures that OpenGL resource cleanup operations in the destructor will always work, as long as this function is called first.

.. seealso:: `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.context`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.doneCurrent`.
