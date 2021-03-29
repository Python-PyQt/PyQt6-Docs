.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6c69018c733f392631b25d2bb486426b

This virtual function is called after each invocation of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`.

When the update mode is set to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.NoPartialUpdate`, there is no difference between this function and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, performing rendering in either of them leads to the same result.

Like :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintUnderGL`, rendering in this function targets the default framebuffer of the window, regardless of the update behavior. It gets called after :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` has returned and the blit (\ :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.PartialUpdateBlit`) or quad drawing (\ :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.PartialUpdateBlend`) has been done.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintUnderGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.UpdateBehavior`.
