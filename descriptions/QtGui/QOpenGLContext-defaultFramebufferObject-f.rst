.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 45c3c35f65b625afab21805421075ede

Call this to get the default framebuffer object for the current surface.

On some platforms (for instance, iOS) the default framebuffer object depends on the surface being rendered to, and might be different from 0. Thus, instead of calling glBindFramebuffer(0), you should call glBindFramebuffer(ctx->) if you want your application to work across different Qt platforms.

If you use the glBindFramebuffer() in QOpenGLFunctions you do not have to worry about this, as it automatically binds the current context's  when 0 is passed.

**Note:** Widgets that render via framebuffer objects, like :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, will override the value returned from this function when painting is active, because at that time the correct "default" framebuffer is the widget's associated backing framebuffer, not the platform-specific one belonging to the top-level window's surface. This ensures the expected behavior for this function and other classes relying on it (for example, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.bindDefault` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.release`).

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`.
